from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def basic_phishing_check(url):
    """Temporary rule-based phishing detection (replace with AI later)"""
    phishing_keywords = ["secure", "verify", "login", "banking", "account", "free", "prize"]
    if any(word in url.lower() for word in phishing_keywords):
        return "Suspicious"
    elif "paypal.com" in url and not url.startswith("https://www.paypal.com"):
        return "Phishing"
    else:
        return "Safe"

@app.route("/check_url", methods=["POST"])
def check_url():
    data = request.get_json()
    url = data.get("url")

    if not url:
        return jsonify({"error": "URL is required"}), 400

    result = basic_phishing_check(url)
    return jsonify({"status": result})

if __name__ == "__main__":
    app.run(debug=True)
