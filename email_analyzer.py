import re

def analyze_email(text):

    result = {}

    suspicious_words = [
        "urgent",
        "verify",
        "account suspended",
        "click here",
        "reset password"
    ]

    result["phishing_words"] = any(word in text.lower() for word in suspicious_words)

    urls = re.findall(r'https?://\S+', text)
    result["links_found"] = urls

    result["many_links"] = len(urls) > 2

    return result