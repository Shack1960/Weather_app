import requests
from django.shortcuts import render
from .models import WeatherData

def index(request):
    # Get all weather data from the database
    weather_data = WeatherData.objects.all()

def weather_view(request):
    # OpenWeatherMap API configuration
    api_key = '22c0893470ed2a52c46c6d80b034c9a7'  # Replace with your OpenWeatherMap API key
    city = 'Nairobi'  # You can change this to any city you like
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    try:
        # Make a GET request to the OpenWeatherMap API
        response = requests.get(url)
        data = response.json()

        # Print response for debugging
        print("API Response:", data)

        if response.status_code == 200:
            # Extract relevant data
            weather_info = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed'],
            }

            # Save the weather data to the database
            WeatherData.objects.create(
                location=weather_info['city'],
                temperature=weather_info['temperature'],
                humidity=weather_info['humidity'],
                wind_speed=weather_info['wind_speed'],
            )

            return render(request, 'weatherapp/weather.html', {'weather': weather_info})
        else:
            error_message = f"API Error: {data.get('message', 'Unknown error')}"
            print(error_message)
            return render(request, 'weatherapp/weather.html', {'error': error_message})

    except Exception as e:
        error_message = f"Error fetching weather data: {str(e)}"
        print(error_message)
        return render(request, 'weatherapp/weather.html', {'error': error_message})
