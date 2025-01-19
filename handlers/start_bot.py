from aiogram import Router
from aiogram.filters import CommandStart, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from configuration.app_state import FSMRegisterUser
from crm.db import add_user

router = Router()


GREETING_MESSAGE = (
    '''
    Привет! Добро пожаловать на Сказочный "Экспресс.
    Для доступа к закрытому каналу вам необходимо:
    - подписаться на каналы А и Б;
    - выложить пост с текстом 'приходите на вебинар'

    Для начала подпишитесь и подтвердите нажатием на кнопку ниже.
    '''
)


@router.message(CommandStart(), StateFilter(default_state))
async def start_bot(message: Message, state: FSMContext):
    user_data = message.from_user
    user_id = user_data.id
    username = user_data.username
    full_name = user_data.full_name

    user_data = (user_id, username, full_name)
    add_user(*user_data)

    subscribed_button = InlineKeyboardButton(
        text='Я подписался(сь)',
        callback_data='subscribed'
    )
    keyboard: list[list[InlineKeyboardButton]] = [[subscribed_button]]
    markup = InlineKeyboardMarkup(inline_keyboard=keyboard)

    await message.answer(GREETING_MESSAGE, reply_markup=markup)
    await state.set_state(FSMRegisterUser.subscribe_channels)
