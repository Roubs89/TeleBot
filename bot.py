import config
import logging

from aiogram import Bot, Dispatcher, executor, types

# задаём уровень логов
logging.basicConfig(level=logging.INFO)

<<<<<<< HEAD:bot.py
# RUN11
bot.polling(none_stop=True)
=======
# инициализация бота
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

# Эхо
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

# запускаем лонг поллинг
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
>>>>>>> 263f4baae07497de60df370f69a33657dcae8f38:main.py
