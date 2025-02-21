from aiogram import Router
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from configuration.app_state import FSMRegisterUser
from crm.db import add_user, fetch_user_by_tg_id
from utils import messages_for_users


router = Router()


@router.message(CommandStart(), StateFilter(default_state))
async def start_bot(message: Message, state: FSMContext):
    user_data = message.from_user
    user_id = user_data.id
    user = fetch_user_by_tg_id(user_id)
    if user:
        return

    username = user_data.username
    full_name = user_data.full_name
    user_data = (user_id, username, full_name)
    add_user(*user_data)

    markup = prepare_inline_keyboard()
    await message.answer(messages_for_users.GREETING_MESSAGE, reply_markup=markup)
    await state.set_state(FSMRegisterUser.subscribe_channels)


def prepare_inline_keyboard() -> InlineKeyboardMarkup:
    subscribed_button = InlineKeyboardButton(
        text='Я подписался(ась)',
        callback_data='subscribed'
    )
    keyboard: list[list[InlineKeyboardButton]] = [[subscribed_button]]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)
    return markup
