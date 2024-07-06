from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = '339e5c1f2509be3a963d6344'
API_URL = f'https://v6.exchangerate-api.com/v6/339e5c1f2509be3a963d6344/latest/USD'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    from_currency = request.form['from_currency'].upper()
    to_currency = request.form['to_currency'].upper()
    try:
        amount = float(request.form['amount'])
    except ValueError:
        return jsonify({'error': 'Invalid amount'})

    response = requests.get(API_URL)
    data = response.json()

    if response.status_code != 200 or 'error' in data:
        return jsonify({'error': 'API request failed'})

    rates = data.get('conversion_rates', {})
    if from_currency not in rates or to_currency not in rates:
        return jsonify({'error': 'Currency not supported'})

    converted_amount = amount * (rates[to_currency] / rates[from_currency])
    return jsonify({'converted_amount': converted_amount})

if __name__ == '__main__':
    app.run(debug=True,port = 6001)
