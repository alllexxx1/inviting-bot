import asyncio

from configuration import app_state
from handlers import check_subscription, managing, start_bot, validate_pass

bot = app_state.bot
dp = app_state.dp

dp.include_router(start_bot.router)
dp.include_router(check_subscription.router)
dp.include_router(validate_pass.router)
dp.include_router(managing.router)


async def main():
    managing.start_scheduler(bot)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
