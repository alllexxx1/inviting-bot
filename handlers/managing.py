from aiogram import Bot, F, Router
from aiogram.exceptions import AiogramError
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import FSInputFile, Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from configuration.logger import get_logger
from configuration.settings import settings
from crm.db import fetch_ineligible_users, update_reminder_count
from crm.utils import prepare_user_data
from utils import messages_for_users


logger = get_logger(__name__)


ADMIN1_ID = settings.ADMIN1_ID
ADMIN2_ID = settings.ADMIN2_ID

router = Router()


@router.message(
    StateFilter(default_state),
    (F.from_user.id.in_({ADMIN1_ID, ADMIN2_ID})) & (F.text.in_({'.', '..'})),
)
async def send_user_data(message: Message):
    user_id = message.from_user.id
    try:
        if message.text == '..':
            report_path = prepare_user_data(txt=True)
            if report_path:
                await message.bot.send_document(
                    chat_id=user_id, document=FSInputFile(report_path)
                )
            else:
                await message.answer('Apparently there are no users yet')
        elif message.text == '.':
            user_data = prepare_user_data(txt=False)
            if user_data:
                await message.answer(user_data)
            else:
                await message.answer('Apparently there are no users yet')
    except (AiogramError, Exception) as e:
        logger.error(f"Failed to send the report: {e}")
        await message.reply(f"Failed to send the report: {e}")


@router.shutdown()
async def stop_bot(bot: Bot):
    await bot.send_message(chat_id=ADMIN1_ID, text="I am done!")


async def fetch_and_send_reminders(bot: Bot):
    users_list = fetch_ineligible_users()

    for user in users_list:
        user_tg_id = user[1]
        reminder_count = user[5]
        if reminder_count:
            try:
                await bot.send_message(
                    chat_id=user_tg_id,
                    text=messages_for_users.REMINDER,
                    disable_notification=True,
                )
                update_reminder_count(user_tg_id)
            except (AiogramError, Exception):
                logger.error(f'Failed to send reminder to {user_tg_id}')


def start_scheduler(bot: Bot):
    scheduler = AsyncIOScheduler()
    scheduler.add_job(fetch_and_send_reminders, 'interval', hours=5, args=[bot])
    scheduler.start()
