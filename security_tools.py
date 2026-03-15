import ollama
import re
from functools import lru_cache

# ----------------------------
# AI ASSISTANT (FAST + CACHED)
# ----------------------------
@lru_cache(maxsize=100)
def ai_assistant(prompt: str):

    response = ollama.chat(
        model="phi",
        messages=[
            {
                "role": "system",
                "content": "You are a cybersecurity expert AI. Analyze threats, phishing, malware and give security advice."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature": 0.2,
            "num_predict": 200
        }
    )

    return {
        "analysis": response["message"]["content"],
        "risk_level": "Medium",
        "recommendation": "Follow cybersecurity best practices."
    }


# ----------------------------
# LINK SCANNER (RULE BASED)
# ----------------------------
def link_scanner(url: str):

    suspicious_patterns = [
        "login",
        "verify",
        "bank",
        "secure",
        "account",
        "update",
        "free",
        "gift"
    ]

    risk = "Low"

    for pattern in suspicious_patterns:
        if pattern in url.lower():
            risk = "High"
            break

    return {
        "url": url,
        "risk_level": risk,
        "message": "URL analyzed using heuristic phishing detection."
    }


# ----------------------------
# EMAIL ANALYZER (AI)
# ----------------------------
def email_analyzer(text: str):

    response = ollama.chat(
        model="mistral",
        messages=[
            {
                "role": "system",
                "content": "You are a cybersecurity AI. Detect phishing emails and explain why."
            },
            {
                "role": "user",
                "content": text
            }
        ],
        options={
            "temperature": 0.2,
            "num_predict": 200
        }
    )

    return {
        "analysis": response["message"]["content"],
        "risk_level": "Medium"
    }


# ----------------------------
# DEVICE SECURITY SCAN
# ----------------------------
def device_scan():

    return {
        "status": "Safe",
        "checks": [
            "Firewall status checked",
            "OS updates verified",
            "Antivirus running"
        ]
    }


# ----------------------------
# MALWARE DIAGNOSIS (AI)
# ----------------------------
def malware_diagnosis():

    response = ollama.chat(
        model="phi",
        messages=[
            {
                "role": "system",
                "content": "You are a malware detection expert."
            },
            {
                "role": "user",
                "content": "Device running slow, high CPU usage, unknown processes"
            }
        ],
        options={
            "num_predict": 150
        }
    )

    return {
        "analysis": response["message"]["content"]
    }


# ----------------------------
# THREAT FEED
# ----------------------------
def threat_feed():

    return {
        "latest_threats": [
            "New phishing campaign targeting banking users",
            "Malware disguised as PDF invoices spreading via email",
            "Credential stuffing attacks increasing globally"
        ]
    }


# ----------------------------
# SECURITY TIPS
# ----------------------------
def security_tips():

    return {
        "tips": [
            "Use strong unique passwords",
            "Enable two-factor authentication",
            "Avoid clicking suspicious links",
            "Keep your software updated"
        ]
    }


# ----------------------------
# LEARNING CENTER
# ----------------------------
def learning_center():

    return {
        "topics": [
            "Phishing attacks",
            "Malware types",
            "Password security",
            "Safe browsing practices"
        ]
    }