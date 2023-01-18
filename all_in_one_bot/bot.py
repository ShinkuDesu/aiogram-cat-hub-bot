import asyncio

from configs.api_key import TOKEN_API_KEY
from aiogram import Bot, Dispatcher
from handlers import cats, other, commands


# Запуск бота
async def main():
    bot = Bot(token=TOKEN_API_KEY)
    dp = Dispatcher()

    dp.include_router(commands.router)
    dp.include_router(cats.router)
    dp.include_router(other.router)

    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
