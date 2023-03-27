import telebot
import webbrowser

bot = telebot.TeleBot('6195281557:AAEkxKpGuojU4M9YN1eOACUUccUw8vVNV1Y')

#start command

@bot.message_handler(commands=['start', 'mail', 'hello'])
def start_fun(message):
    bot.send_message(message.chat.id, f'Hello!, {message.from_user.first_name} {message.from_user.last_name}! \nHow are you today?')

@bot.message_handler(commands=['site', 'web', 'website'])
def site(message):
    webbrowser.open('https://www.google.com')

@bot.message_handler(commands=['myid'])
def start_fun(message):
    bot.send_message(message.chat.id, message)

@bot.message_handler(commands=['help'])
def start_fun(message):
    bot.send_message(message.chat.id, '<b>Help</b> <a href="www.google.com">information</a>: ', parse_mode='html')



# Formatig text from user
@bot.message_handler()
def info(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id,
                         f'Привет, {message.from_user.first_name} {message.from_user.last_name}! \nКак дела заебал?')
    elif message.text.lower() == "id":
        bot.reply_to(message, f'ID: {message.from_user.id}')
    else:
        bot.send_message(message.chat.id, '<b>Help</b> <a href="www.google.com">information</a>: ', parse_mode='html')


# Keeping the programm running.
bot.polling(none_stop=True)