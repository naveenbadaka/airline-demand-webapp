# Airline Demand Web App 

## Overview
A Flask-based web app that analyzes airline booking trends using the AviationStack API.  
This tool helps visualize top flight routes and trends based on real-time airline data.

## Features
-  Top airline route analysis based on frequency
-  Interactive data visualization using Chart.js
-  Clean, processed insights using Pandas
-  Simple web interface with form-based input

## Setup Instructions

1.  Replace `YOUR_API_KEY` in `app.py` with your AviationStack API key
   ```python
   params = {"access_key": "YOUR_API_KEY", "limit": limit}
2. Install the required packages:

    pip install -r requirements.txt

3.  Run the Flask app:

    python app.py

4. Open your browser at:

    http://127.0.0.1:8000
    
## Demo

> Screenshots from the working web app:

###  Home Page
![Home Page](screenshots/Home/)

###  Results Page
![Results Page](screenshots/results/)
