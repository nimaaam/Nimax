from aiogram import Router, types

router = Router()

@router.message(commands=["about"])
async def about_handler(message: types.Message):
    await message.answer("🧑‍💼 درباره Nimax:\nNimax یک پروژه مینی‌اپ و بات تلگرام برای قرعه‌کشی و سرگرمیه!")
