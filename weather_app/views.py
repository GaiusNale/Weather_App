import requests
from django.shortcuts import render
from .forms import WeatherForm
from .keysus import keysus

def get_weather_data(city):
    api_key = keysus 
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def weather(request):
    """
    This function handles the weather request.
    It processes the form data and renders the weather.html template.
    """
    # If the request method is POST
    if request.method == 'POST':
        # Create a form instance with the POST data
        form = WeatherForm(request.POST)
        # Check if the form is valid
        if form.is_valid():
            city = form.cleaned_data['city'] # Get the city from the form data
            weather_data = get_weather_data(city) # Get the weather data for the city

            # If the request to the API was successful
            if weather_data['cod'] == 200:
                temperature = weather_data['main']['temp'] # Get the temperature from the weather data
                description = weather_data['weather'][0]['description'] # Get the description from the weather data
                humidity = weather_data['main']['humidity'] # Get the humidity from the weather data
                wind_speed = weather_data['wind']['speed'] # Get the wind speed from the weather data
                visibility = weather_data.get('visibility', 'N/A') # Get the visibility from the weather data
                country = weather_data['sys']['country']
                context = {'temperature': temperature,
                            'description': description, 
                            'city': city,
                            'country': country,
                            'humidity': humidity, 
                            'wind_speed': wind_speed,
                            'visibility': visibility} # Create the context dictionary
            else:
                context = {'error_message': 'City not found'} # If the city is not found, create an error message

            # Render the weather.html template with the context
            return render(request, 'weather_app/weather.html', context)

    # If the request method is not POST, create a new form instance
    else:
        form = WeatherForm()

    # Render the weather.html template with the form
    return render(request, 'weather_app/weather.html', {'form': form})
