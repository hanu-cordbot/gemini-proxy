import os, requests
from flask import Flask, request

app = Flask(__name__)
GEMINI_KEY = os.getenv("GEMINI_KEY", "")

@app.route("/", methods=["POST"])
def relay():
    r = requests.post(
        "https://generativelanguage.googleapis.com/v1beta/models/"
        "gemini-2.5-flash:generateContent",
        params={"key": GEMINI_KEY},
        headers={"Content-Type": "application/json"},
        data=request.data,
        timeout=60,
    )
    return r.content, r.status_code, {"Content-Type": "application/json"}
