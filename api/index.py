# api/index.py  – Vercel “HTTP Function” style
import os, json, urllib.request, urllib.error

GEMINI_URL = (
    "https://generativelanguage.googleapis.com/v1beta/models/"
    "gemini-2.5-flash:generateContent?key=" + os.environ["GEMINI_KEY"]
)

def handler(request):
    try:
        with urllib.request.urlopen(
            urllib.request.Request(
                GEMINI_URL,
                data=request.body,
                headers={"Content-Type": "application/json"},
            ),
            timeout=60,
        ) as resp:
            data = resp.read()
        return data.decode(), resp.status, {"Content-Type": "application/json"}
    except urllib.error.HTTPError as e:
        return e.read().decode(), e.code, {"Content-Type": "application/json"}
