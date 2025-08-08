# 🛡️ SmartHoneypot

SmartHoneypot is an **educational honeypot system** that monitors and logs malicious activity targeting **SSH** and **HTTP** services.  
It includes **real-time alerts**, an **interactive dashboard**, **IP blacklisting**, and **GeoIP tracking**.

---

## 🚀 Features

- **SSH Honeypot** – Captures login attempts and executed commands.
- **HTTP Honeypot** – Logs suspicious HTTP requests (method, path, user-agent, etc.).
- **IP Blacklisting** – Automatically adds malicious IPs to a blacklist file.
- **GeoIP Lookup** – Enriches IP logs with geolocation and ISP data.
- **Real-time Alerts** – Sends notifications via Discord and Email.
- **Dashboard UI** – View, filter, and search logs by IP, User-Agent, service, and date.
- **Log Storage** – Structured JSON logs for easy analysis.

---

## 📂 Project Structure

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

---

## 🛠 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/SmartHoneypot.git
cd SmartHoneypot
```
### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Configure settings
Edit config/settings.json to set:

- Alert credentials (Discord webhook, Email SMTP)
- Blacklist file path
- Dashboard port
- Ensure your logs/ directory exists and is writable.

### ▶ Running the Honeypots
Running Both Honeypot (Recommended)
```bash
cd SmartHoneypot
python run.py
```
For SSH Honeypot
```bash
python honeypot/ssh_honey.py
```
For HTTP Honeypot
```bash
python honeypot/http_honey.py
```
📊 Start the Dashboard
```bash
cd dashboard
python app.py
```
Open in your browser: http://localhost:5000

📌 Usage

- Filter logs by service, date, IP, or User-Agent from the dashboard.
- Blacklist IPs manually by adding them to blacklist.txt (auto for repeat offenders).
- View GeoIP details for location and ISP.
- Receive real-time alerts via Discord and/or email.

> [!CAUTION]
> This project is for educational purposes only.
> 
> Running a honeypot may attract real-world attacks.
> 
> Deploy in a controlled environment or VPS — never on a production system.

