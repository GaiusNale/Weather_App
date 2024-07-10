# Nimbus 🌤️

## Description
Nimbus is a web application that provides real-time weather information for any city in the world. Users can search for a city to get the current temperature, weather description, humidity, wind speed, and visibility. The app also displays a background image related to the city queried.

## Features
- **City Search:** Allows users to search for the current weather in any city.
- **Weather Details:** Displays temperature, weather description, humidity, wind speed, and visibility.
- **Background Image:** Dynamically changes the background image based on the current queried city.
- **Mobile Optimization:** The app is optimized for mobile devices.

## Technologies Used
- **Django:** Backend framework to handle server-side logic.
- **HTML/CSS/JavaScript:** Frontend technologies for rendering the user interface.
- **Bootstrap:** CSS framework for responsive design.
- **Unsplash API:** Provides background images based on the city searched.
- **OpenWeatherMap API:** Fetches real-time weather data for the searched city.

## Live Demo
You can access the live demo of the Weather App [here](https://weather-app-5ip9.onrender.com).

## Setup Instructions
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/weather-app.git
    cd weather-app
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    Create a `.env` file in the root directory of the project and add the following variables:
    ```env
    SECRET_KEY=your_secret_key
    UNPLASH_KEY=your_unsplash_api_key
    OPENAPI=your_openweathermap_api_key
    ```

5. Run the Django development server:
    ```bash
    python manage.py runserver
    ```

6. Open your browser and navigate to `http://127.0.0.1:8000` to see the app in action.

## Project Structure
```
weather_project/
├── weather_app/
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       └── script.js
│   ├── templates/
│   │   └── index.html
│   ├── views.py
│   ├── models.py
│   └── urls.py
├── weather_project/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── .env
├── manage.py
└── requirements.txt
```

## Contributing
Feel free to submit issues or pull requests if you have any suggestions or improvements.

