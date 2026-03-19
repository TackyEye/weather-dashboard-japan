from flask import Flask, render_template, jsonify
from weather_api import get_weather_forecast
from datetime import datetime
import json

app = Flask(__name__)

@app.route('/')
def dashboard():
    """Render the main dashboard page"""
    return render_template('dashboard.html')

@app.route('/api/weather')
def weather_data():
    """API endpoint that returns current weather data"""
    forecast_data = get_weather_forecast()
    
    if forecast_data is None:
        return jsonify({'error': 'Failed to fetch weather data'}), 500
    
    # Extract first hourly temperature reading
    try:
        hourly_data = forecast_data.get('hourly', {})
        temperatures = hourly_data.get('temperature_2m', [])
        time_data = hourly_data.get('time', [])
        
        current_temp = temperatures[0] if temperatures else 'N/A'
        current_time = time_data[0] if time_data else 'N/A'
        
        return jsonify({
            'temperature': current_temp,
            'time': current_time,
            'location': 'Tokyo, Japan',
            'latitude': 35.6897,
            'longitude': 139.6922,
            'last_updated': datetime.now().isoformat(),
            'hourly_temps': temperatures[:24]  # Next 24 hours
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, port=port, host='0.0.0.0')
