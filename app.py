
from flask import Flask, render_template, request
import requests
import pandas as pd

app = Flask(__name__)

def fetch_flight_data(limit=50):
    url = "http://api.aviationstack.com/v1/flights"
    params = {"access_key": "YOUR_API_KEY", "limit": limit}
    response = requests.get(url, params=params)
    return response.json()

def process_data(raw_data):
    flights = raw_data['data']
    df = pd.json_normalize(flights)
    df['route'] = df['departure.iata'] + ' - ' + df['arrival.iata']
    top_routes = df['route'].value_counts().head(5)
    return top_routes.to_dict()

@app.route('/', methods=["GET"])
def index():
    print("INDEX PAGE LOADED")
    return render_template("index.html")

@app.route('/results', methods=["POST"])
def results():
    limit = int(request.form.get("limit", 50))
    raw_data = fetch_flight_data(limit)
    insights = process_data(raw_data)
    labels = list(insights.keys())
    values = list(insights.values())
    return render_template("results.html", labels=labels, values=values)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

