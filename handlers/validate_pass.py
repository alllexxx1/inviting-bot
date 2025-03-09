import asyncio
from typing import Any

from aiogram import Bot, F, Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from configuration.app_state import FSMRegisterUser
from utils import messages_for_users
from utils.full_access import give_full_access
from utils.personal_invite_link import send_personal_link
from utils.ticket_sender import send_stamped_ticket_to_eligible_user

router = Router()


@router.message(StateFilter(FSMRegisterUser.send_valid_pass), F.photo)
async def validate_pass(message: Message, bot: Bot, state: FSMContext) -> Any:
    user_id = message.from_user.id
    picture_to_validate = await message.bot.get_file(message.photo[-1].file_id)
    path_to_picture = f'staticfiles/images/{user_id}.png'
    await bot.download_file(picture_to_validate.file_path, path_to_picture)
    await give_full_access(user_id)
    await state.clear()

    await message.answer(messages_for_users.SCREENSHOT_IS_BEING_PROCESSED_MESSAGE)
    await asyncio.sleep(57600)

    await send_stamped_ticket_to_eligible_user(message)
    await send_personal_link(message)


@router.message(StateFilter(FSMRegisterUser.send_valid_pass))
async def warning_wrong_format(message: Message):
    await message.answer(messages_for_users.NOT_PICTURE_MESSAGE)
