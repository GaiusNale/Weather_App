# import requests 
# from django.shortcuts import render
# from .forms import WeatherForm

# def get_weather_data(city):
#     api_key = "419b87c5611ad660453b06003a68f583"
#     base_url = 'http://api.openweathermap.org/data/2.5/weather'
#     parameters = {'q': city, 'appid': api_key, 'units': 'metric'}
#     response =  requests.get(base_url, params=parameters)
#     data = response.json()
#     return data 

# def weather(request):
#     if request.method == 'POST':
#         form = WeatherForm(request.POST)
#         if form.is_valid():
#             city = form.cleaned_data['city']
#             weather_data = get_weather_data(city)

#             if weather_data['cod'] == 200:
#                 temperature = weather_data['main']['temp']
#                 description = weather_data['weather'][0]['description']
#                 humidity = weather_data['main']['humidity']
#                 wind_speed = weather_data['wind']['speed']
#                 visibility = weather_data.get('visibility', 'N/A')        
#                 context = {'Temperature': temperature, 'Description': description, 'City': city, 'Humidity': humidity, 'Wind speed': wind_speed, 'Visibility': visibility}

#             else:
#                 context = {'error': 'City not found.'}

#             return render(request, 'weather_app/weather.html', context)

#     else:
#         form = WeatherForm()

#     return render(request, 'weather_app/weather.html', {'form': form})

import requests
from django.shortcuts import render
from .forms import WeatherForm

def get_weather_data(city):
    api_key = '419b87c5611ad660453b06003a68f583'  # Replace with your OpenWeatherMap API key
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
