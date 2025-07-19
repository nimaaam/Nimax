from aiogram import Router, types

router = Router()

@router.message(commands=["rules"])
async def rules_handler(message: types.Message):
    await message.answer(
        "📜 قوانین Nimax:\n"
        "۱. هر کاربر فقط یک حساب مجاز دارد.\n"
        "۲. رعایت احترام به دیگران الزامیست.\n"
        "۳. هرگونه تخلف = حذف از قرعه‌کشی!"
    )
