from django.db import models

# Create your models here.
from django.db import models

class WeatherData(models.Model):
    location = models.CharField(max_length=100)  # City or location name
    temperature = models.FloatField()  # Temperature in Celsius
    humidity = models.IntegerField()  # Humidity percentage
    wind_speed = models.FloatField()  # Wind speed in km/h
    description = models.CharField(max_length=255)  # Weather description (e.g., "Sunny", "Cloudy")
    recorded_at = models.DateTimeField(auto_now_add=True)  # Timestamp of data collection

    def __str__(self):
        return f"{self.location} - {self.temperature}°C, {self.description}"
