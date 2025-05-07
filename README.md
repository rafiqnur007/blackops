# 🕵️‍♂️ BLACK OPS – Real-Time Web Threat Hunter

![Black Ops Banner](https://i.postimg.cc/bYbRT5Fp/A-banner-image-for-a-cybersecurity-tool-named-Bla.png)

**Black Ops** is a Python-based security tool designed for real-time threat detection and automatic blocking of malicious IPs targeting web servers. It monitors access logs (e.g., Nginx, Apache), detects suspicious behavior like SQL injection scanners or brute-force attempts, and dynamically blocks the source IPs using `iptables`.

---

## 🚀 Features

- ✅ Real-time log monitoring
- 🚫 Automatic IP blocking for suspicious activity
- 🔍 Detects tools like sqlmap, nikto, nmap, acunetix
- 🧠 Customizable detection patterns and thresholds
- 📁 Lightweight and simple to deploy
- 🔐 Built for SOC analysts, CTF teams, and security pros

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/black-ops.git
cd black-ops
pip install .
```

> 🔧 Requires Python 3.6+ and root access to use `iptables`

---

## ⚙️ Configuration

Edit `blackops/config.py` to customize:
- `LOG_PATH` – location of your web server's access log
- `BLOCK_THRESHOLD` – number of suspicious hits before blocking an IP
- `SUSPICIOUS_PATTERNS` – regex patterns to detect attacks

---

## 🛡️ Usage

```bash
sudo python3 scripts/run_blackops.py
```

- The script will continuously monitor the log file.
- When an IP triggers enough alerts (e.g., 10 suspicious lines), it will be auto-blocked.
- Blocked IPs are saved in `denylist.txt`.

---

## 📂 File Structure

```
black-ops/
├── blackops/
│   ├── __init__.py
│   ├── config.py
│   └── core.py
│
├── scripts/
│   └── run_blackops.py
│
├── denylist.txt
├── requirements.txt
├── LICENSE
├── .gitignore
└── README.md
```

---

## 🧠 Future Ideas

- Slack/Discord alert integration
- Web-based dashboard (Flask)
- Threat intelligence lookups (AbuseIPDB API)
- Windows support via `netsh` or `firewall`

---

## 📜 License

This project is licensed under the [MIT License](./LICENSE).

---

### 👨‍💻 Author

**Black Ops** was built with 🔥 by **Rafiq Nur**, cybersecurity enthusiast and CTF team leader.  
> Follow updates and features as the project grows on GitHub!
