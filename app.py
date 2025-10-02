import os
import logging
from flask import Flask, request
import requests

# Configure logging for debugging
logging.basicConfig(level=logging.DEBUG)

# Create Flask application
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET",
                                "dev-secret-key-change-in-production")

# Telegram configuration from environment variables
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")


@app.route('/webhook', methods=['POST'])
def webhook():
    """Webhook endpoint to receive TradingView alerts and send to Telegram"""
    try:
        data = request.json
        alert_message = data.get('message',
                                 'No message provided by TradingView')

        # Log the received alert for debugging
        app.logger.info(f"Received alert: {alert_message}")

        # Check if Telegram credentials are configured
        if not TELEGRAM_BOT_TOKEN or not CHAT_ID:
            app.logger.error("Telegram credentials not configured")
            return {"error": "Telegram credentials not configured"}, 500

        # Send message to Telegram
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {"chat_id": CHAT_ID, "text": alert_message}

        response = requests.post(url, json=payload)

        if response.status_code == 200:
            app.logger.info("Alert sent to Telegram successfully")
            return {"status": "success", "message": "Alert sent to Telegram"}
        else:
            app.logger.error(f"Failed to send to Telegram: {response.text}")
            return {"error": "Failed to send to Telegram"}, 500

    except Exception as e:
        app.logger.error(f"Error processing webhook: {str(e)}")
        return {"error": "Internal server error"}, 500


@app.route('/', methods=['GET'])
def index():
    """Simple status page"""
    return {
        "status": "TradingView to Telegram Webhook Service",
        "webhook_url": "/webhook",
        "method": "POST",
        "configured": bool(TELEGRAM_BOT_TOKEN and CHAT_ID)
    }


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return {"status": "healthy"}


@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors"""
    return {"error": "Endpoint not found"}, 404


@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    app.logger.error(f'Server Error: {error}')
    return {"error": "Internal server error"}, 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
