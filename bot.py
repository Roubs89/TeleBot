import config
import logging

from aiogram import Bot, Dispatcher, executor, types

# задаём уровень логов
logging.basicConfig(level=logging.INFO)

# инициализация бота
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

# Эхо
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

# запускаем лонг поллинг
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
