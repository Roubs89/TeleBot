import config
import logging

from aiogram import Bot, Dispatcher, executor, types

# задаём уровень логов
logging.basicConfg(level=logging.INFO)

# инициализация бота
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

# Эхо
@dp.massage_handler()
async def echo(message: types.Message):
    await mesage.answer(message.text)

# запускаем лонг поллинг
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
