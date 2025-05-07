LOG_PATH = "/var/log/nginx/access.log"
BLOCK_THRESHOLD = 10
DENYLIST_FILE = "denylist.txt"

SUSPICIOUS_PATTERNS = [
    r"(sqlmap|acunetix|nikto|nmap)",
    r"404",
]
