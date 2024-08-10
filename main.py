import requests

# Here goes the actual API key
API_KEY = 'YOUR_API_KEY'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'


def get_weather(city_name: str) -> None:
    """Fetches the weather data for the specified city."""
    try:
        # Construct the final API URL
        url = BASE_URL + "q=" + city_name + "&appid=" + API_KEY + "&units=metric"  # TODO: configurable?

        # Send GET request to the API
        response = requests.get(url)

        # Raise an exception for (hopefully not) bad status codes
        response.raise_for_status()

        # Parse the JSON data
        weather_data = response.json()

        # Extract infos
        main = weather_data['main']
        wind = weather_data['wind']
        weather = weather_data['weather'][0]

        # Display the information
        print(f"\nWeather in {city_name}:")
        print(f"Temperature: {main['temp']}°C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Weather: {weather['description'].capitalize()}")
        print(f"Wind Speed: {wind['speed']} m/s")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")


if __name__ == "__main__":

    # Get city name input from user
    city_name = input("Enter the city name: ")
    get_weather(city_name)