import requests
from tkinter import *

Zip = input("Enter your zipcode")
apiURL = 'https://api.openweathermap.org/data/2.5/weather?q=32536&appid=f4051fd923412d7b460bfbbaebd1143b&units=metric'
res = requests.get(apiURL)
data = res.json()
tempCel = data['main']['temp']
tempF = format((tempCel * 9/5) + 32, ".1f")

print(tempF)