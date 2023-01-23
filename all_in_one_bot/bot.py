import asyncio

from configs.api_key import TOKEN_API_KEY
from aiogram import Bot, Dispatcher
from handlers import (
    cats,
    echo,
    commands,
    groups_games,
    usernames,
    checkin,
)
from middlewares.weekend import WeekendCallbackMiddleware


# Запуск бота
async def main():
    bot = Bot(token=TOKEN_API_KEY)
    dp = Dispatcher()

    dp.callback_query.outer_middleware(WeekendCallbackMiddleware())

    dp.include_router(commands.router)
    dp.include_router(cats.router)
    dp.include_router(usernames.router)
    dp.include_router(groups_games.router)
    dp.include_router(checkin.router)

    dp.include_router(echo.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print('Starting')
    asyncio.run(main())
