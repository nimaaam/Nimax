from aiogram import Router, types

router = Router()

@router.message(commands=["help"])
async def help_handler(message: types.Message):
    await message.answer(
        "📋 راهنما:\n"
        "/start - شروع\n"
        "/help - راهنما\n"
        "/about - درباره ما\n"
        "/rules - قوانین\n"
        "/features - امکانات\n"
        "/support - پشتیبانی\n"
        "/feedback - ارسال پیام/بازخورد"
    )
