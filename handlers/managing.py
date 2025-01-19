from aiogram import Bot, F, Router
from aiogram.exceptions import AiogramError
from aiogram.filters import StateFilter
from aiogram.fsm.state import default_state
from aiogram.types import FSInputFile, Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from crm.db import fetch_ineligible_users
from crm.utils import prepare_user_data
from configuration.logger import get_logger
from configuration.settings import settings

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
            await message.bot.send_document(chat_id=user_id, document=FSInputFile(report_path))
        elif message.text == '.':
            user_data = prepare_user_data(txt=False)
            await message.answer(user_data)
    except (AiogramError, Exception) as e:
        await message.reply(f"Failed to sand the report: {e}")


@router.message(StateFilter(default_state))
async def echo(message: Message):
    await message.answer('Спасибо за ваше сообщение!')


@router.shutdown()
async def stop_bot(bot: Bot):
    await bot.send_message(chat_id=ADMIN1_ID, text="I am done")


async def fetch_and_send_reminders(bot: Bot):
    users_list = fetch_ineligible_users()

    for user_id in users_list:
        user_id = user_id[0]
        try:
            await bot.send_message(chat_id=user_id, text="Закончите все шаги и получите доступ к крутейшему контенту!")
        except Exception:
            print(f'Failed to send reminder to {user_id}')


def start_scheduler(bot: Bot):
    scheduler = AsyncIOScheduler()
    scheduler.add_job(fetch_and_send_reminders, 'interval', hours=6, args=[bot])
    scheduler.start()
