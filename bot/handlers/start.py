from aiogram import Router, types

router = Router()

@router.message(commands=["start"])
async def start_handler(message: types.Message):
    await message.answer("سلام حاج نیما! به Nimax خوش اومدی 👋")
