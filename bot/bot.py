import asyncio
from aiogram import Bot, Dispatcher, types
from config import API_TOKEN
import handlers

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(commands=["start"])
async def start_cmd(message: types.Message):
    await handlers.cmd_start(message)

@dp.message()
async def all_messages(message: types.Message):
    if message.text == "🛒 خرید بلیت":
        await handlers.handle_buy(message)
    elif message.text == "📜 قوانین":
        await handlers.handle_rules(message)
    elif message.text == "🆘 پشتیبانی":
        await handlers.handle_support(message)
    else:
        await handlers.handle_unknown(message)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
