from flask import Flask, render_template, request, jsonify
import joblib
import re
import pandas as pd

app = Flask(__name__)

# Load the pre-trained model
model = joblib.load('ai_models/url_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check_url', methods=['POST'])
def check_url():
    data = request.get_json()
    url = data.get('url')
    
    # Extract features from the URL
    features = extract_features(url)
    df_features = pd.DataFrame([features])
    
    # Predict using the model
    prediction = model.predict(df_features)[0]
    
    if prediction == 1:
        status = "Phishing 🔴"
    else:
        status = "Safe 🟢"
    
    return jsonify({'status': status})

def extract_features(url):
    """ Extract features from URL to match the trained AI model """
    features = {
        'NumDots': url.count('.'),
        'UrlLength': len(url),
        'AtSymbol': int('@' in url),
        'NumDash': url.count('-'),
        'NumPercent': url.count('%'),
        'NumQueryComponents': url.count('?'),
        'IpAddress': int(re.search(r'\d+\.\d+\.\d+\.\d+', url) is not None),
        'HttpsInHostname': int('https' in url.split('/')[2] if len(url.split('/')) > 2 else 0),
        'PathLevel': url.count('/'),
        'PathLength': len(url.split('/')[-1]),
        'NumNumericChars': len(re.findall(r'\d', url))
    }
    return features

if __name__ == '__main__':
    app.run(debug=True)
