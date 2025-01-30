# weather_app
  
A simple Django-based weather application that provides current weather data, including temperature, humidity, and wind speed, for different locations. The app is designed to track weather data and display it in a user-friendly format.

## Features


- Displays weather data including temperature, humidity, and wind speed.

- Stores weather data in a database (SQLite).

- Allows the user to view the weather data of different locations.

## Installation

### Prerequisites

- Python 3.12 or higher

- Django 5.1.5

- Virtual environment (recommended)

### Setup

1. **Clone the repository:**

   ```bash

   git clone https://github.com/Shack1960/weather_app.git

   cd weather_app

Create and activate a virtual environment:

  
For Windows:

  
    ``bash

python -m venv weatherenv

weatherenv\Scripts\activate
```

  

For macOS/Linux:

    
```bash

python3 -m venv weatherenv

source weatherenv/bin/activate

```

  

```bash
Install the required dependencies

pip install -r requirements.txt

Run database migrations:

python manage.py makemigrations

python manage.py migrate

Run the Django development server:

python manage.py runserver
```

Visit the app in your browser:

Open your browser and go to http://127.0.0.1:8000/ to view the weather data.

  
  

### How It Works


Models: The WeatherData model is used to store the weather data for each location. It includes fields for location name, temperature, humidity, and wind speed.

Views: The weatherview function retrieves weather data and sends it to the template. This data is then displayed in a table format.

URL Routing: The urls.py file in weatherapp defines the URL route to the weather view, which is the main page of the application.

Templates: The weather.html template displays the weather data in a table format.

Future Enhancements:

Allow users to input different locations to view weather data for.

Display additional weather information like forecasts and air quality.

Data Visualizations and Historical Insights.

Personalized Weather Recommendations.