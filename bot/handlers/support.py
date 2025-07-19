from aiogram import Router, types

router = Router()

@router.message(commands=["support"])
async def support_handler(message: types.Message):
    await message.answer("🆘 پشتیبانی Nimax:\nسوالی داشتی یا به مشکل خوردی؟ به @nimax_support پیام بده.")
