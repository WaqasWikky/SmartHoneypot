# SmartHoneypot

SmartHoneypot is an educational honeypot system that monitors and logs malicious activity targeting **SSH** and **HTTP** services. It includes real-time alerts, an interactive dashboard, IP blacklisting, and GeoIP tracking.

## Features

- **SSH Honeypot** – Captures login attempts and commands.
- **HTTP Honeypot** – Logs suspicious HTTP requests (method, path, user-agent, etc.).
- **IP Blacklisting** – Automatically adds malicious IPs to a blacklist file.
- **GeoIP Lookup** – Enriches IP logs with geolocation and ISP data.
- **Real-time Alerts** – Sends notifications via Discord and email.
- **Dashboard UI** – View, filter, and search logs by IP, User-Agent, service, and date.
- **Log Storage** – Structured JSON logs for easy analysis.

## Project Structure

SmartHoneypot/
│
├── alerts/ # Alert handlers (Discord, Email)
├── config/ # Configuration files
├── dashboard/ # Flask web UI
├── honeypot/ # SSH and HTTP honeypot scripts
├── intel/ # GeoIP lookup and IP intelligence
├── logs/ # Captured logs (http_log.json, ssh_log.json, etc.)
├── run.py # Main entry point
└── README.md # This file

## Installation

1. **Clone the repository**

   git clone https://github.com/yourusername/SmartHoneypot.git
   cd SmartHoneypot




2. **Install dependencies**

bash
Copy
Edit
pip install -r requirements.txt
Configure settings

Edit config/settings.json for alert credentials, blacklist paths, and dashboard port.

Ensure your logs/ directory exists and is writable.

Run the honeypots

bash
Copy
Edit
python honeypot/ssh_honey.py
python honeypot/http_honey.py
Start the dashboard

bash
Copy
Edit
cd dashboard
python app.py
Open http://localhost:5000 in your browser.

Usage
Filter logs by service, date, IP, or User-Agent from the dashboard.

Blacklist IPs by adding them to blacklist.txt (automated for repeated offenders).

View GeoIP details in the logs for origin location and ISP.

Receive alerts on Discord and/or email when an attack is detected.

Disclaimer
This project is for educational purposes only. Running a honeypot may attract real-world attacks.
Deploy in a controlled environment or VPS, and do not run on a production system.
