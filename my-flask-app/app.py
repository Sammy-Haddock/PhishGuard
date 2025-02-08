from flask import Flask, render_template, request, jsonify # type: ignore

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check_url', methods=['POST'])
def check_url():
    data = request.get_json()
    url = data.get('url')
    
    # Placeholder for AI model logic
    # Replace this with actual AI model integration
    if "phishing" in url:
        status = "Phishing 🔴"
    elif "suspicious" in url:
        status = "Suspicious 🟠"
    else:
        status = "Safe 🟢"
    
    return jsonify({'status': status})

if __name__ == '__main__':
    app.run(debug=True)