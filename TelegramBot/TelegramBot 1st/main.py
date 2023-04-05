import telebot
import webbrowser
from telebot import types


bot = telebot.TeleBot('6195281557:AAEkxKpGuojU')


# Adding buttons to text field

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Visit GIT')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Delete photo')
    btn3 = types.KeyboardButton('Edit text')
    markup.row(btn2, btn3)


    # bot.send_message(message.chat.id, 'Holla', reply_markup=markup)
    # Sending file instead of replying

    file = open('img/1.png', 'rb')

    bot.send_photo(message.chat.id, file, reply_markup=markup)


    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'Visit GIT':
        webbrowser.open('https://github.com/dmussin')
    elif  message.text == 'Deleted photo':
        bot.send_message(message.chat.id, 'Deleted')



#start command

# @bot.message_handler(commands=['start', 'mail', 'hello'])
# def start_fun(message):
#     bot.send_message(message.chat.id, f'Hello!, {message.from_user.first_name} {message.from_user.last_name}! \nHow are you today?')

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



# File sending handler
# @bot.message_handler(content_types=['photo'])
# def get_photo(message):
#     # Buttons
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('Visit GIT', url='https://github.com/dmussin'))
#     markup.add(types.InlineKeyboardButton('Delete photo', callback_data='delete'))
#     markup.add(types.InlineKeyboardButton('Edit text', callback_data='edit'))
#     bot.reply_to(message, 'Such a great photo!', reply_markup=markup)


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    # Buttons
    markup = types.InlineKeyboardMarkup()

    # Change layout of the buttons
    btn1 = types.InlineKeyboardButton('Visit GIT', url='https://github.com/dmussin')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Delete photo', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Edit text', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'Such a great photo!', reply_markup=markup)
    print("4M9YN1eOACUUccUw8vVNV1Y")

# Callback Handler
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)






# Keeping the programm running.
bot.polling(none_stop=True)
