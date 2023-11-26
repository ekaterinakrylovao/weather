# weather

## Overview
WeatherAPI is a simple Flask-based backend application that provides weather information using the OpenWeatherMap API.

## Local Deployment

### Prerequisites
- Python (version 3.9)
- Flask
- Requests

### Installation
1. Clone the repository:

    ```bash
    git clone https://github.com/ekaterinakrylovao/weather.git
    cd weather
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Configuration
1. Open the `app.py` file in a text editor.

2. Replace the placeholder for the OpenWeatherMap API key (`OPENWEATHERMAP_API_KEY`) with your actual key:

    ```python
    OPENWEATHERMAP_API_KEY = "your_actual_api_key_here"
    ```

### Running the Application
1. Start the Flask application:

    ```bash
    python app.py
    ```

2. The application will be accessible at `http://127.0.0.1:5000`.

## Application Logic

### Endpoints

1. **`/current_info/{cityname}`**
   - Returns full information about the current weather in the chosen city, including longitude, latitude, and additional details.

2. **`/current_weather/{cityname}`**
   - Returns information about the current weather in the chosen city, including cloudiness, temperature, and feels-like temperature.

3. **`/weather_forecast/{cityname}`**
   - Returns the weather forecast for the chosen city.

### Request Examples

- Use tools like `curl` or Postman to test the endpoints.
  ```bash
  curl http://127.0.0.1:5000/current_info/London
  ```
  ```bash
  curl http://127.0.0.1:5000/current_weather/London
  ```
  ```bash
  curl http://127.0.0.1:5000/weather_forecast/London
  ```
  
  Import the [Postman Collection](https://api.postman.com/collections/31407178-5986d90c-64fd-4896-9684-30f6fd4400a1?access_key=PMAT-01HG5X3AF2PVW5JMA7VH28VGW2) into your Postman environment.
