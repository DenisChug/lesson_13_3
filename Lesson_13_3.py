# aiogram 3.15 python 3.12
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command, Message

api = '7740609310:AAE0HSOBjD4QOZDAP7EyxSaV-omMbdS-8iI'
bot = Bot(token=api)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("")
    print('Привет! Я бот помогающий твоему здоровью.' )

@dp.message(F.text)
async def msg_urban(message: Message):
    await message.answer('Введите команду /start, чтобы начать общение.')
    print('Введите команду /start, чтобы начать общение.')


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())