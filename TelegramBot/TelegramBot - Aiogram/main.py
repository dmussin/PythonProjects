from aiogram import Bot, Dispatcher, executor, types


# Creating Bot
bot = Bot("")

dispatcher_bot = Dispatcher(bot)


@dispatcher_bot.message_handler(commands=['start', 'hello'])
# You can track the messages by types @dispatcher_bot.message_handler(content_types=['photo']) or text, video etc
async def start(message: types.Message):
    # await bot.send_message(message.chat.id, "Hello")
    # await message.answer("Hello")
    await message.reply('holllllllll')

    # Replying with the photo.
    #file = open('/some.png', 'rb')
    #await message.answer_photo(file)


# Buttons
@dispatcher_bot.message_handler(commands=['inline'])
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(types.InlineKeyboardButton('Site', url='google.com'))
    markup.add(types.InlineKeyboardButton('Holla', callback_data='Ahoy'))
    await message.reply('Some Buttons Dude!', reply_markup=markup)


#Buttons Func
@dispatcher_bot.callback_query_handler()
async def callback(call):
    await call.message.answer(call.data)



@dispatcher_bot.message_handler(commands=['reply'])
async def reply(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Website'))
    markup.add(types.KeyboardButton('Help'))
    await message.answer('Another Hello With One time keyboard', reply_markup=markup)



# Keeping bot running
executor.start_polling(dispatcher_bot)