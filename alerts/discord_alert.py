import requests

def send_discord_alert_http(ip, data):
    webhook_url = "Your Discord URL Here"

    message = f"🚨 **Honeypot Hit!**\n- IP: `{ip}`\n- Input: `{data.strip()}`"

    payload = {
        "content": message
    }

    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()
    except Exception as e:
        print(f"[x] Failed to send Discord alert: {e}")

#For SSH alerts
def send_discord_alert_ssh(ip, data):
    webhook_url = "Your Discord URL Here"

    message = f"🚨 **Honeypot Hit!**\n- IP: `{ip}`\n- Input: `{data.strip()}`"

    payload = {
        "content": message
    }

    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()
    except Exception as e:
        print(f"[x] Failed to send Discord alert: {e}")
