from aiogram import Router, types

router = Router()

@router.message(commands=["feedback"])
async def feedback_handler(message: types.Message):
    await message.answer("💬 پیام یا انتقاد خودتو اینجا بنویس، تیم Nimax می‌خونه و جواب می‌ده!")
