from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from safecore_backend.security_tools import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ai")
def ai(prompt: str):
    return {"response": ai_assistant(prompt)}

@app.get("/scan-link")
def scan_link(url: str):
    return link_scanner(url)

@app.post("/analyze-email")
def analyze_email(text: str):
    return email_analyzer(text)

@app.get("/device-scan")
def device_scan_api():
    return device_scan()

@app.get("/malware")
def malware():
    return malware_diagnosis()

@app.get("/threat-feed")
def threats():
    return threat_feed()

@app.get("/tips")
def tips():
    return security_tips()

@app.get("/learning")
def learning():
    return learning_center()