from aiogram import Bot, Dispatcher
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from configuration.settings import settings

storage = MemoryStorage()

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher(storage=storage)


class FSMRegisterUser(StatesGroup):
    subscribe_channels = State()
    send_valid_pass = State()
