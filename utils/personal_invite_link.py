from aiogram.types import ChatInviteLink, Message

from configuration.logger import get_logger
from configuration.settings import settings

logger = get_logger(__name__)

CHANNEL_ID = settings.CHANNEL_ID


async def generate_personal_link(
        message: Message, user_id: int, chanel_id: str
) -> ChatInviteLink | None:
    try:
        invite_link: ChatInviteLink = await message.bot.create_chat_invite_link(
            chat_id=chanel_id,
            name=f'Invite for {user_id}',
            member_limit=1,
        )
        return invite_link

    except Exception as e:
        msg = f'Failed to create invite link: {e}'
        logger.error(msg)
        return None


async def send_personal_link(message: Message) -> None:
    user_id = message.from_user.id
    invite_link = await generate_personal_link(message, user_id, CHANNEL_ID)

    if invite_link:
        await message.answer(invite_link.invite_link)
    else:
        await message.answer('Что-то пошло не так. Напишите нам для'
                             'получения персональной ссылки.')
