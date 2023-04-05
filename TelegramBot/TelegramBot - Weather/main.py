import json

import telebot
import sqlite3
from telebot import types
import requests


bot = telebot.TeleBot('6195281557:7e9c87e8780a5b90b8b2fe39e5068592:AAEkxKpGuojU4M9YN1eOACUUccUw8vVNV1Y')
API_OPEN_WEATHER = ''



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hey! Nice to see you! Please type your city:')


# Tracking the text typed by user
@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    print(city)
    # Sending request using url
    weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_OPEN_WEATHER}&units=metric')
    # bot.reply_to(message, f'Weather Now: {weather.json()}') #- PURE JSON

    # Checking status:
    if weather.status_code == 200:
        data = json.loads(weather.text)
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        bot.reply_to(message, f'Weather Now: {temp} °C\nDescription: {description.capitalize()}')
        print(f'Weather Now: {temp} °C\nDescription: {description}.')

        # Images
        if description == 'clear sky':
            image = 'sunny.png'
        elif description == 'broken clouds':
            image = 'cloud.png'
        elif description == 'few clouds':
            image = 'clear-sky.png'
        elif description == 'rain' or description == 'shower rain':
            image = 'rainy-day.png'
        elif description == 'show':
            image = 'snowfall.png'

        file = open('./img/' + image, 'rb')
        bot.send_photo(message.chat.id, file)

    else:
        bot.reply_to(message, 'Ooops No City Detected! Check the spelling')


bot.polling(none_stop=True)