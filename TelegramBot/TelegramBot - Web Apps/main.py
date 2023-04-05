from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo


# Creating Bot
bot = Bot("6195281557:AAEkxKpGuojU4M9YN1eOACUUccUw8vVNV1Y")
dispatcher_bot = Dispatcher(bot)

# webapp
@dispatcher_bot.message_handler(commands=['webapp'])
async  def webapp(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Open Web App', web_app=WebAppInfo(url='https://github.com/dmussin')))
    await message.answer('Hey!', reply_markup=markup)


# Keeping bot running
executor.start_polling(dispatcher_bot)