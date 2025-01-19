import os

from aiogram.types import FSInputFile, Message
from configuration.logger import get_logger
from utils.picture_processor import stamp_ticket

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logger = get_logger(__name__)


async def send_stamped_ticket_to_eligible_user(message: Message):
    user_id = message.from_user.id
    try:
        stamped_ticket_path = str(stamp_ticket(user_id))
        ticket = FSInputFile(stamped_ticket_path)
        await message.bot.send_photo(chat_id=user_id, photo=ticket)
    except Exception as e:
        msg = f'Failed to stamp the ticket: {e}'
        # logger.error(msg)
        logger.debug("Value is %s" % msg)
        await message.reply("'Что-то пошло не так. Напишите нам для получения билета.")
