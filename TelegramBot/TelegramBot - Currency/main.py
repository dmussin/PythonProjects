import telebot
from currency_converter import CurrencyConverter
from telebot import types



bot = telebot.TeleBot('')

currency = CurrencyConverter()
total_amount = 0

print(currency.currencies)

@bot.message_handler(commands=['cur'])
def cur(message):
    bot.send_message(message.chat.id, "Hey there! Please type a amount:")
    bot.register_next_step_handler(message, amount)

def amount(message):
    global total_amount

    # Exception handler
    # try:
    #   total_amount = int(message.text.strip())
    #   if int(total_amount) <= 0:
    #       raise ValueError("Error: Entered number is not positive.")
    #   else:
    #       print("Input is a positive number.")
    # except ValueError as e:
    #     print(e)
    #     bot.send_message(message.chat.id, "Wrong format, please type a positive amount only! Please try again.")
    #     bot.register_next_step_handler(message, amount)
    #     return

    try:
      total_amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, "Wrong format, please type a positive amount only! Please try again.")
        bot.register_next_step_handler(message, amount)
        return

    try:
        if total_amount <= 0:
          raise ValueError("Error: Entered number is not positive.")
        else:
            # Buttons
            markup = types.InlineKeyboardMarkup(row_width=2)
            btn1 = types.InlineKeyboardButton('CZK/USD', callback_data='czk/usd')
            btn2 = types.InlineKeyboardButton('USD/CZK', callback_data='usd/czk')
            btn3 = types.InlineKeyboardButton('CZK/EUR', callback_data='czk/eur')
            btn4 = types.InlineKeyboardButton('EUR/CZK', callback_data='eur/czk')
            btn5 = types.InlineKeyboardButton('Other', callback_data='else')

            markup.add(btn1, btn2, btn3, btn4, btn5)

            bot.send_message(message.chat.id, "Pick the Currencies:", reply_markup=markup)
    except ValueError as e:
        print(e)
        bot.send_message(message.chat.id, "Please type a positive amount only! Try again.")
        bot.register_next_step_handler(message, amount)
        return


# Buttons functionality
@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    if call.data != 'else':
        # Getting values of the data from btn
        values = call.data.upper().split('/')
        res = currency.convert(total_amount, values[0], values[1])
        bot.send_message(call.message.chat.id, f'Result: {round(res, 2)}. You can type the amount again.')
        # Registering new func
        bot.register_next_step_handler(call.message, amount)
    else:
        # Getting a new pair of currencies
        bot.send_message(call.message.chat.id, 'Type your currencies pair using "/" (ex. KZT/GBP)')
        bot.register_next_step_handler(call.message, my_currency)

def my_currency(message):
    try:
        value = message.text.upper().split('/')
        res = currency.convert(total_amount, value[0], value[1])
        bot.send_message(message.chat.id, f'Result: {round(res, 2)}. You can type the amount again.')
        bot.register_next_step_handler(message, amount)
    except Exception:
        bot.send_message(message.chat.id, f'Something went wrong! Please try again.')
        bot.register_next_step_handler(message, amount)

bot.polling(none_stop=True)