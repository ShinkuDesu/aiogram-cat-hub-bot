import asyncio
import aiosqlite

from configs.api_key import TOKEN_API_KEY
from aiogram import Bot, Dispatcher
from handlers import (
    get_cat,
    upload_cat,
    start,
    echo,
    commands,
    groups_games,
    usernames,
    checkin,
    ordering_food,
    common,
)
from middlewares.weekend import WeekendCallbackMiddleware
from aiogram.fsm.storage.memory import MemoryStorage

# Запуск бота
async def main():
    bot = Bot(token=TOKEN_API_KEY)

    dp = Dispatcher(storage=MemoryStorage())
    # dp.callback_query.outer_middleware(WeekendCallbackMiddleware())
    # # новый импорт
    # from aiogram.dispatcher.fsm.strategy import FSMStrategy

    # async def main():
    # # тут код
    # dp = Dispatcher(storage=MemoryStorage(), fsm_strategy=FSMStrategy.CHAT)
    # # тут тоже код


    dp.include_router(start.router)
    dp.include_router(upload_cat.router)
    dp.include_router(get_cat.router)
    # dp.include_router(usernames.router)
    # dp.include_router(groups_games.router)
    # dp.include_router(checkin.router)
    # dp.include_router(ordering_food.router)
    # dp.include_router(common.router)

    # dp.include_router(echo.router)
    
    db = await create_db()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(
        bot,
        allowed_updates=dp.resolve_used_update_types(),
        db=db,
    )

    # Подгрузка списка админов
    # admins = await bot.get_chat_administrators(config.main_chat_id)
    # admin_ids = {admin.user.id for admin in admins}

    # await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types(), admins=admin_ids)


async def create_db():
    db = await aiosqlite.connect('bot.db')
    await db.execute(
        '''
        CREATE TABLE IF NOT EXISTS cats(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_id INTEGER NOT NULL UNIQUE,
            upload_by INTEGER NOT NULL,
            rating INTEGER DEFAULT 0
        )
        '''
    )
    await db.commit()
    return db

if __name__ == "__main__":
    print('Starting')
    
    asyncio.run(main())
