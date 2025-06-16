import asyncio
from aiogram import Bot, Dispatcher

bot =  Bot(token='TOKEN')
dp = Dispatcher

async def main():
    await dp.stop_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())