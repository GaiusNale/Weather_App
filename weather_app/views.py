import requests
from django.shortcuts import render
from .forms import WeatherForm
from .keysus import keysus
from .keysus import unplash_api_key

def get_weather_data(city):
    api_key = keysus
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key, 'units': 'metric'}
    response = requests.get(base_url, params=params)
    data = response.json()
    return data

def get_unsplash_image(city):
    api_key = unplash_api_key
    base_url = "https://api.unsplash.com/search/photos"
    params = {'query': f"{city} landscape", 'client_id': api_key, 'per_page': 3, 'orientation': 'landscape'}
    response = requests.get(base_url, params=params)
    data = response.json()
    if data['results']:
        image_url = data['results'][0]['urls']['regular']
        photographer = data['results'][0]['user']['name']
        return image_url, photographer
    else:
        return None, None

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
            image_url, photographer = get_unsplash_image(city) # Get the image URL and photographer name for the city

            # If the request to the API was successful
            if weather_data['cod'] == 200:
                temperature = weather_data['main']['temp'] # Get the temperature from the weather data
                description = weather_data['weather'][0]['description'] # Get the description from the weather data
                humidity = weather_data['main']['humidity'] # Get the humidity from the weather data
                wind_speed = weather_data['wind']['speed'] # Get the wind speed from the weather data
                visibility = weather_data.get('visibility', 'N/A') # Get the visibility from the weather data
                country = weather_data['sys']['country']
                

                # Assign emojis to certain weather conditions
                emoji = {
                    "clear sky": "☀️",
                    "few clouds": "⛅️",
                    "scattered clouds": "☁️",
                    "broken clouds": "☁️☁️  ",
                    "light rain": "🌧️",
                    "rain": "🌧️",
                    "thunderstorm": "⛈️",
                    "snow": "❄️",
                    "mist": "💦",
                }
                
                # Get the emoji for the weather description
                description_emoji = emoji.get(description.lower(), "❓")

                context = {'temperature': temperature,
                            'description': f"{description} {description_emoji}", 
                            'city': city,
                            'country': country,
                            'humidity': humidity, 
                            'wind_speed': wind_speed,
                            'visibility': visibility,
                            'image_url': image_url,
                            'photographer': photographer} # Create the context dictionary
            else:
                context = {'error_message': 'City not found'} # If the city is not found, create an error message

            # Render the weather.html template with the context
            return render(request, 'weather_app/weather.html', context)

    # If the request method is not POST, create a new form instance
    else:
        form = WeatherForm()

    # Render the weather.html template with the form
    return render(request, 'weather_app/weather.html', {'form': form})


