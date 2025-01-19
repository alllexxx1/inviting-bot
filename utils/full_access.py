from aiogram.types import Message

from crm.db import is_user_eligible, update_eligibility


async def give_full_access(user_id):
    update_eligibility(user_id)


async def check_eligibility(message: Message):
    user_id = message.from_user.id
    eligibility = is_user_eligible(user_id)

    if eligibility:
        await message.answer('Ok!')
    else:
        await message.answer('Не Ok!')
