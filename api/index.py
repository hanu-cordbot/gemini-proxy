# api/index.py
import os, requests, flask
app = flask.Flask(__name__)
GEMINI_KEY = os.environ["GEMINI_KEY"]

@app.route("/", methods=["POST"])
def relay():
    rsp = requests.post(
        f"https://generativelanguage.googleapis.com/v1beta/models/"
        f"gemini-2.5-flash:generateContent?key={GEMINI_KEY}",
        headers={"Content-Type": "application/json"},
        data=flask.request.data,
        timeout=60,
    )
    return (rsp.content, rsp.status_code, {"Content-Type": "application/json"})
