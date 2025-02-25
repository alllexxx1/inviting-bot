from aiogram import Bot, F, Router
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    CallbackQuery,
    Message
)

from configuration.app_state import FSMRegisterUser
from configuration.logger import get_logger
from configuration.settings import settings
from handlers.start_bot import prepare_inline_keyboard
from utils import messages_for_users
from utils.full_access import give_full_access
from utils.personal_invite_link import send_personal_link
from utils.ticket_sender import send_stamped_ticket_to_eligible_user

router = Router()
logger = get_logger(__name__)

CHANNEL1_TO_CHECK = settings.CHANNEL1_TO_CHECK
CHANNEL2_TO_CHECK = settings.CHANNEL2_TO_CHECK


@router.callback_query(
    StateFilter(FSMRegisterUser.subscribe_channels), F.data.in_(['subscribed'])
)
async def check_tg_channels_subscription(
    callback: CallbackQuery, bot: Bot, state: FSMContext
):
    user_id = callback.from_user.id
    try:
        # channel_1 = await bot.get_chat_member(CHANNEL1_TO_CHECK, user_id)
        # channel_2 = await bot.get_chat_member(CHANNEL2_TO_CHECK, user_id)
        # if channel_1.status == 'member' and channel_2.status == 'member':

        await give_full_access(user_id)
        await send_stamped_ticket_to_eligible_user(callback)
        await send_personal_link(callback.message, user_id)
        await callback.message.delete()
        await state.clear()

        # else:
        #     markup = prepare_inline_keyboard()
        #     await callback.message.answer(
        #         messages_for_users.NOT_SUBSCRIBED_MESSAGE,
        #         disable_web_page_preview=True,
        #         reply_markup=markup,
        #         parse_mode='HTML'
        #     )
    except Exception as e:
        logger.error(f'Failed to check subscription: {e}')
        await callback.message.answer(messages_for_users.GENERIC_ERROR_MESSAGE)


@router.message(StateFilter(FSMRegisterUser.subscribe_channels))
async def warning_not_subscribed_press(message: Message):
    markup = prepare_inline_keyboard()
    await message.answer(
        messages_for_users.BUTTON_IS_NOT_PRESSED_MESSAGE, reply_markup=markup
    )
