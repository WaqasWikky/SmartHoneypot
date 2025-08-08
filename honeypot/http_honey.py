from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime
import json
import os
from alerts.discord_alert import send_discord_alert_http
from intel.ip_lookup import lookup_ip
from alerts.email_alert import send_email_alert

LOG_FILE = "logs/http_log.json"
PORT = 8080
BLACKLIST_FILE = "blacklist.txt"

def ensure_log_dir():
    os.makedirs("logs", exist_ok=True)

def load_blacklist():
    try:
        with open(BLACKLIST_FILE, "r") as f:
            return set(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        return set()

class HoneyRequestHandler(BaseHTTPRequestHandler):
    blacklist = load_blacklist()

    def is_blacklisted(self, ip):
        return ip in self.blacklist

    def log_attempt(self, method):
        ip = self.client_address[0]
        if self.is_blacklisted(ip):
            print(f"[BLOCKED] Ignoring request from blacklisted IP: {ip}")
            return

        path = self.path
        user_agent = self.headers.get('User-Agent', '')
        timestamp = datetime.now().isoformat()

        if path == "/favicon.ico":
            return

        print(f"[DEBUG] Logging HTTP attack from {ip} to {path}")
        ip_info = lookup_ip(ip) or {
            "country": "Unknown", "region": "", "city": "", "isp": "", "org": ""
        }

        try:
            with open(LOG_FILE, "r") as f:
                logs = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            logs = []

        logs.append({
            "ip": ip,
            "timestamp": timestamp,
            "service": "HTTP",
            "method": method,
            "path": path,
            "user_agent": user_agent,
            "geo": ip_info
        })

        with open(LOG_FILE, "w") as f:
            json.dump(logs, f, indent=4)

        # Alerts
        alert_msg = (
            f"🚨 **HTTP Honeypot Hit!**\n"
            f"- IP: `{ip}`\n"
            f"- Method: `{method}` Path: `{path}`\n"
            f"- UA: `{user_agent}`\n"
            f"- Location: {ip_info['city']}, {ip_info['country']}\n"
            f"- ISP: {ip_info['org']}"
        )
        send_discord_alert_http(ip, alert_msg)
        send_email_alert("🚨 HTTP Honeypot Hit Detected!", alert_msg)

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<h1>404 Not Found</h1>")
        self.log_attempt("GET")

    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"<h1>Login failed</h1>")
        self.log_attempt("POST")

def start_http_honeypot():
    ensure_log_dir()
    server = HTTPServer(('', PORT), HoneyRequestHandler)
    print(f"[+] HTTP Honeypot running on port {PORT}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[+] HTTP honeypot stopped.")
        server.server_close()

if __name__ == "__main__":
    start_http_honeypot()
