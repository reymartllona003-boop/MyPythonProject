import requests
from urllib.parse import quote
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Weather App")
root.geometry("400x300")    

label_city = tk.Label(root, text="Enter City Name:")
label_city.pack(pady=10)

entry_city = tk.Entry(root, width=30)
entry_city.pack(pady=5)

def get_weather():
    city = entry_city.get().strip()
    
    if city == "":
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    city_encoded = quote(city)
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_encoded}&appid=0be691296a4d81f81f3f61c20be09fee"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        city_name = data["name"]
        country = data["sys"]["country"]
        temp_c = data["main"]["temp"] - 273.15
        description = data["weather"][0]["description"].title()
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        result_text = (f"Weather in {city_name}, {country}\n"
                       f"Condition: {description}\n"
                       f"Temperature: {temp_c:.1f}°C\n"
                       f"Humidity: {humidity}%\n"
                       f"Wind Speed: {wind_speed} m/s")

        label_result.config(text=result_text)
    else:
        messagebox.showerror("Error", f"Cannot fetch data for '{city}'. Status code: {response.status_code}")

# Button to fetch weather
button_get = tk.Button(root, text="Get Weather", command=get_weather)
button_get.pack(pady=10)

# Label to show result
label_result = tk.Label(root, text="", justify="left")
label_result.pack(pady=10)
root.mainloop()

