from aiogram import Router, types

router = Router()

@router.message(commands=["features"])
async def features_handler(message: types.Message):
    await message.answer(
        "✨ امکانات Nimax:\n"
        "🎲 قرعه‌کشی\n"
        "🛒 خرید بلیت\n"
        "📜 مشاهده قوانین\n"
        "🆘 پشتیبانی\n"
        "💬 ارسال بازخورد"
    )
