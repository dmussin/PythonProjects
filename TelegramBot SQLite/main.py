import telebot
import sqlite3
from telebot import types


bot = telebot.TeleBot('6195281557:AAEkxKpGuojU4M9YN1eOACUUccUw8vVNV1Y')
name = None

# start command
@bot.message_handler(commands=['start'])
def start(message):
    # Creating a sql file
    conn = sqlite3.connect('mybd.sql')
    cur = conn.cursor()

    # Creating new table
    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')
    # Sync
    conn.commit()
    # Close
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Hey, let me register you - type your Name')
    bot.register_next_step_handler(message, user_name)

def user_name(message):
    # Getting text from user
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Type your password')
    bot.register_next_step_handler(message, user_pass)


def user_pass(message):
    # Getting password from user
    password = message.text.strip()

    # Connecting to BD to register a user
    conn = sqlite3.connect('mybd.sql')
    cur = conn.cursor()

    cur.execute('INSERT INTO users (name, pass) VALUES ("%s", "%s")' % (name, password))

    # Sync
    conn.commit()
    # Close
    cur.close()
    conn.close()


    # Button
    markup = types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('List of Users', callback_data='user_list'))

    # Sending a message
    bot.send_message(message.chat.id, 'Registred', reply_markup=markup)


# Callback Data
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('mybd.sql')
    cur = conn.cursor()
    # Getting all data from users
    cur.execute('SELECT * FROM users')
    # Returning all records
    users = cur.fetchall()

    #
    info = ''
    for el in users:
        info += f'ID: {el[0]} - Name: {el[1]}- Password: {el[2]}\n'

    # Close
    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)
    print(info)

# Keeping the programm running.
bot.polling(none_stop=True)