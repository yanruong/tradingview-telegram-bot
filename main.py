from flask import Flask, request
import requests, os, logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Read Telegram credentials from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

if not BOT_TOKEN or not CHAT_ID:
    app.logger.error("Telegram credentials not configured")

def send_to_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text}
    response = requests.post(url, data=payload)
    if response.status_code != 200:
        app.logger.error(f"Failed to send to Telegram: {response.text}")
    return response

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    message = data.get("text")
    if not message:
        app.logger.info("Received alert: No message provided by TradingView")
        message = "⚠️ No message provided in TradingView alert"
    else:
        app.logger.info(f"Received alert: {message}")

    if BOT_TOKEN and CHAT_ID:
        send_to_telegram(message)
    else:
        app.logger.error("Telegram credentials not configured")

    return {"status": "ok"}

@app.route('/ping', methods=['GET'])
def ping():
    return {"status": "alive"}
