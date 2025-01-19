from aiogram import Bot, F, Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from configuration.app_state import FSMRegisterUser
from configuration.logger import get_logger
from configuration.settings import settings

router = Router()
logger = get_logger(__name__)

CHANNEL_TO_CHECK = settings.CHANNEL_TO_CHECK


@router.callback_query(
    StateFilter(FSMRegisterUser.subscribe_channels), F.data.in_(['subscribed'])
)
async def check_tg_channels_subscription(
    callback: CallbackQuery, bot: Bot, state: FSMContext
):
    user_id = callback.from_user.id
    try:
        member = await bot.get_chat_member(CHANNEL_TO_CHECK, user_id)
        if member.status == 'member':
            await callback.message.delete()
            await callback.message.answer(
                'Отлично. Теперь отправьте скриншот вашего поста, пожалуйста.'
            )
            await state.set_state(FSMRegisterUser.send_valid_pass)
        else:
            await callback.message.answer(
                'Вы не подписаны. Попробуйте еще раз.'
                'Если считаетк, что прозошла ошибка напишите нам.'
            )
    except Exception as e:
        msg = f'Failed to check subscription: {e}'
        logger.error(msg)
        await callback.answer('Что-то пошло не так. Напишите нам.')


@router.message(StateFilter(FSMRegisterUser.subscribe_channels))
async def warning_not_subscribed_press(message: Message):
    await message.answer('Пожалуйста, пользуйтесь кнопкой для подтверждения подписки')
