import asyncio
import aiosqlite

from configs.api_key import TOKEN_API_KEY
from aiogram import Bot, Dispatcher
from handlers import (
    get_cat,
    upload_cat,
    start
)
from aiogram.fsm.storage.memory import MemoryStorage


async def main():
    bot = Bot(token=TOKEN_API_KEY)

    dp = Dispatcher(storage=MemoryStorage())


    dp.include_router(start.router)
    dp.include_router(upload_cat.router)
    dp.include_router(get_cat.router)
    
    db = await create_db()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(
        bot,
        allowed_updates=dp.resolve_used_update_types(),
        db=db,
    )


async def create_db():
    db = await aiosqlite.connect('bot.db')
    await db.execute(
        '''
        CREATE TABLE IF NOT EXISTS cats(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cat_msg BLOB,
            rating INTEGER DEFAULT 0
        )
        '''
    )
    await db.commit()
    return db

if __name__ == "__main__":
    print('Starting')
    
    asyncio.run(main())
