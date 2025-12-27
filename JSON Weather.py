import requests 
from urllib.parse import quote 
import tkinter as tk
from tkinter import messagebox

while True:
    City = input("Enter City Name: ")

    if City == "exit":
        print("Goodbye!")
        break

    url = f"https://api.openweathermap.org/data/2.5/weather?q={City}&appid=0be691296a4d81f81f3f61c20be09fee"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        City_Name = data['name']
        Temperature = data['main']['temp'] - 273.15
        Description = data['weather'][0]['description']
        Wind = data['wind']['speed']
        Humidity = data['main']['humidity']

       


        print(f"City: {City_Name}")
        print(f"Temperature: {Temperature}")
        print(f"Weather Description: {Description}")

        print(f"{City_Name} has a temperature of {Temperature:.1f}°C with {Description} descriptions.")
        print(f"{City_Name} has a wind speed of {Wind} m/s and humidity of {Humidity}%.")
        print("-" * 40)
    else: 
        print(f"Error to retrieve data: {response.status_code}")