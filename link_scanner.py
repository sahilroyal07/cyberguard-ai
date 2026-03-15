import re
import requests
from urllib.parse import urlparse

def scan_url(url):

    result = {}

    parsed = urlparse(url)

    # Check HTTPS
    result["https"] = parsed.scheme == "https"

    # Suspicious keywords
    suspicious = ["login", "verify", "bank", "secure", "update"]

    result["suspicious_keywords"] = any(word in url.lower() for word in suspicious)

    # URL length
    result["long_url"] = len(url) > 75

    # IP address in URL
    ip_pattern = r'\d+\.\d+\.\d+\.\d+'
    result["ip_address"] = bool(re.search(ip_pattern, url))

    return result