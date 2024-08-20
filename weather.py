from tkinter import *
import requests
from PIL import Image, ImageTk


url = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "eeae5bbc65094b06a41eb83de8e60e38"
icon_url = "https://openweathermap.org/img/wn/{}@2x.png"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "lang":"tr"}
    response = requests.get(url, params=params).json()
    if response:
        city_temp = response["name"].capitalize()
        country_temp = response["sys"]["country"]
        temp_min = int(int(response["main"]["temp"]) - 273.15)
        icon_temp = response["weather"][0]["icon"]
        condition_temp = response["weather"][0]["description"]
        return [city_temp, country_temp, temp_min, icon_temp, condition_temp]

def main():
    city = city_entry.get()
    weather = get_weather(city)
    if weather:
        location_Label.config(text=f"{weather[0]} in {weather[1]}")
        temp_label.config(text=f"{weather[2]} Celsius ")
        condition_Label.config(text=f"{weather[3]}")
        icon = ImageTk.PhotoImage(Image.open(requests.get(icon_url.format(weather[3]), stream=True).raw))
        iconLabel.config(image=icon)
        iconLabel.image = icon


app = Tk()
app.geometry("300x450")
app.title("Weather App")

city_entry = Entry(app, justify="center")
city_entry.pack(fill=BOTH,  ipady=10, padx=10, pady=5)
city_entry.focus()

search_button = Button(app, text="Search",font=("Arial",15),command=main)
search_button.pack(fill=BOTH, ipady=10, padx=20)

iconLabel = Label(app)
iconLabel.pack()

location_Label = Label(app, font=("Arial",15))
location_Label.pack()

temp_label = Label(app, font=("Arial",15,"bold"))
temp_label.pack()

condition_Label = Label(app, font=("Arial",15))
condition_Label.pack()




app.mainloop()







