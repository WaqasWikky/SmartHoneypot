from flask import Flask, render_template
import json, os
from collections import Counter, defaultdict
from datetime import datetime

app = Flask(__name__)

def load_logs(filename):
    path = os.path.join("..", "logs", filename)  # go one level up
    print(f"[*] Trying to load: {path}")
    try:
        with open(path, "r") as f:
            data = json.load(f)
            print(f"[+] Loaded {len(data)} entries from {filename}")
            return data
    except Exception as e:
        print(f"[!] Failed to load {filename}: {e}")
        return []

def group_by_day(logs):
    daily_counts = defaultdict(int)
    for log in logs:
        try:
            dt = datetime.fromisoformat(log["timestamp"])
            date_str = dt.strftime("%Y-%m-%d")
            daily_counts[date_str] += 1
        except:
            continue
    return dict(sorted(daily_counts.items()))

@app.route("/")
def dashboard():
    http_logs = load_logs("http_log.json")
    ssh_logs = load_logs("ssh_log.json")

    # Count hits per service
    service_data = {
        "HTTP": len(http_logs),
        "SSH": len(ssh_logs)
    }

    # Top IPs
    ip_counter = Counter()
    ip_counter.update(log["ip"] for log in http_logs)
    ip_counter.update(log["ip"] for log in ssh_logs)
    top_ips = [{"ip": ip, "count": count} for ip, count in ip_counter.most_common(5)]

    # Daily timeline
    http_daily = group_by_day(http_logs)
    ssh_daily = group_by_day(ssh_logs)
    all_dates = sorted(set(http_daily.keys()) | set(ssh_daily.keys()))
    attack_timeline = {
        "dates": all_dates,
        "http": [http_daily.get(date, 0) for date in all_dates],
        "ssh": [ssh_daily.get(date, 0) for date in all_dates]
    }

    return render_template(
        "dashboard.html",
        http_logs=http_logs,
        ssh_logs=ssh_logs,
        service_data=service_data,
        top_ips=top_ips,
        attack_timeline=attack_timeline
    )

if __name__ == "__main__":
    app.run(debug=True)
