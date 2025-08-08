import socket
import json
from datetime import datetime
from alerts.discord_alert import send_discord_alert_ssh
from intel.ip_lookup import lookup_ip
from alerts.email_alert import send_email_alert
import os

LOG_FILE = "logs/ssh_log.json"
PORT = 2222  # Fake SSH port
BLACKLIST_FILE = "blacklist.txt"

def load_blacklist():
    try:
        with open(BLACKLIST_FILE, "r") as f:
            return set(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        return set()

def log_connection(ip, data=""):
    timestamp = datetime.now().isoformat()
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
        "service": "SSH",
        "data": data.strip(),
        "geo": ip_info
    })

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)

    print(f"[+] SSH attack from {ip} logged with geolocation")

    # Alerts
    alert_msg = (
        f"🚨 **SSH Honeypot Hit!**\n"
        f"- IP: `{ip}`\n"
        f"- Location: {ip_info['city']}, {ip_info['country']}\n"
        f"- Org: {ip_info['org']}\n"
        f"- Data: `{data.strip()}`"
    )
    send_discord_alert_ssh(ip, alert_msg)
    send_email_alert("🚨 SSH Honeypot Hit Detected!", alert_msg)

def start_ssh_honeypot():
    blacklist = load_blacklist()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', PORT))
    s.listen(5)
    print(f"[+] SSH Honeypot running on port {PORT}")

    while True:
        client, addr = s.accept()
        ip = addr[0]

        if ip in blacklist:
            print(f"[BLOCKED] Connection attempt from blacklisted IP: {ip}")
            client.close()
            continue

        print(f"[!] Connection from {ip}")
        client.send(b"SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.3\r\n")

        client.settimeout(5.0)
        data = b""
        try:
            while True:
                chunk = client.recv(1024)
                if not chunk:
                    break
                data += chunk
        except socket.timeout:
            pass
        except Exception as e:
            print(f"[x] Error receiving data: {e}")

        decoded = data.decode(errors="ignore")
        print(f"[+] Data from {ip}: {repr(decoded)}")
        log_connection(ip, decoded)
        client.close()

if __name__ == "__main__":
    start_ssh_honeypot()
