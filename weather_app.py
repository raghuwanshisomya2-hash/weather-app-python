import requests

def get_weather(city):
    api_key = "YOUR_API_KEY_HERE"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            print("City not found. Please try again.")
            return

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        print("\n------ Weather Report ------")
        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {description.capitalize()}")

    except Exception as e:
        print("Error fetching weather data:", e)


print("------ Weather App ------")
city_name = input("Enter city name: ")
get_weather(city_name)
