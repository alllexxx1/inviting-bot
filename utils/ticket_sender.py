import os

from aiogram.types import FSInputFile, Message

from configuration.logger import get_logger
from crm import db
from utils import messages_for_users
from utils.picture_processor import stamp_ticket

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logger = get_logger(__name__)


async def send_stamped_ticket_to_eligible_user(message: Message):
    user_id = message.from_user.id
    user_personal_number = db.fetch_user_db_id(user_id)
    try:
        stamped_ticket_path = str(stamp_ticket(user_personal_number))
        ticket = FSInputFile(stamped_ticket_path)
        await message.bot.send_photo(chat_id=user_id, photo=ticket)
    except Exception as e:
        logger.error(f'Failed to stamp the ticket: {e}')
        await message.answer(messages_for_users.GENERIC_ERROR_MESSAGE)
