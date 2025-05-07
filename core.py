import re
import time
import subprocess
from collections import defaultdict
from blackops import config

ip_activity = defaultdict(int)
blocked_ips = set()

def tail_log(path):
    with open(path, "r") as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield line

def is_suspicious(line):
    return any(re.search(p, line, re.IGNORECASE) for p in config.SUSPICIOUS_PATTERNS)

def extract_ip(line):
    return line.split(" ")[0]

def block_ip(ip):
    if ip in blocked_ips:
        return
    print(f"[!] Blocking IP: {ip}")
    subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"])
    with open(config.DENYLIST_FILE, "a") as f:
        f.write(f"{ip}\n")
    blocked_ips.add(ip)

def load_blocked_ips():
    try:
        with open(config.DENYLIST_FILE, "r") as f:
            for line in f:
                blocked_ips.add(line.strip())
    except FileNotFoundError:
        pass

def monitor():
    print("🚨 Black Ops is running...")
    load_blocked_ips()
    for line in tail_log(config.LOG_PATH):
        if is_suspicious(line):
            ip = extract_ip(line)
            ip_activity[ip] += 1
            print(f"[+] Suspicious activity from {ip} ({ip_activity[ip]} hits)")
            if ip_activity[ip] >= config.BLOCK_THRESHOLD:
                block_ip(ip)
