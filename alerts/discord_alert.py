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
    webhook_url = "https://discord.com/api/webhooks/1402052029756608629/p8-vxKQh1CvyjgaX_s-loCN-lI6GejdGgpd5jpXXStz6CvbMpbNk-ChEjOvVKY_kPN8G"

    message = f"🚨 **Honeypot Hit!**\n- IP: `{ip}`\n- Input: `{data.strip()}`"

    payload = {
        "content": message
    }

    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()
    except Exception as e:
        print(f"[x] Failed to send Discord alert: {e}")
