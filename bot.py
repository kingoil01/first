import asyncio
import logging
from aiogram import Bot, Dispatcher, types

logging.basicConfig(level=logging.INFO)

bot = Bot(token='6033497571:AAFxFBD7h5MrYhHjbqGLw_uTdsu2zdVinE0')

dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer('Hello world!')

@dp.message_handler(commands=['test1'])
async def cmd_test1(message: types.Message):
    await message.reply('test1')

@dp.message_handler(commands=['test2'])
async def cmd_test1(message: types.Message):
    await message.reply('test2')

async def main():
    await dp.start_polling(bot)

if __name__=='__main__':
    asyncio.run(main())