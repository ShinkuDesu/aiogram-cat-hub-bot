import random

from aiogram import (
    Router,
    F,
)
from aiogram.filters import (
    Command,
)
from aiogram.types import (
    Message,
    CallbackQuery,
)
from keyboards.get_cat import get_cats_ikb, CatsCallbackFactory
from aiosqlite import Connection
import pickle


router = Router()


@router.message(
    Command(commands=['cat']),
)
async def cat_cmd(message: Message, db: Connection):
    cat_data = random.choice(await db.execute_fetchall('SELECT * FROM cats'))
    cat_msg = pickle.loads(cat_data[1])
    await message.answer_photo(
        photo=cat_msg.photo[-1].file_id,
        caption=cat_msg.caption,
        reply_markup=get_cats_ikb(),
    )


@router.callback_query(
    CatsCallbackFactory.filter(F.action=='more_cats')
)
async def more_cats_fab(callback: CallbackQuery, db: Connection):
    await cat_cmd(callback.message, db)
    await callback.answer()


@router.callback_query(
    CatsCallbackFactory.filter(F.action=='like')
)
async def like_fab(callback: CallbackQuery):
    await callback.answer()


@router.callback_query(
    CatsCallbackFactory.filter(F.action=='like')
)
async def dislike_fab(callback: CallbackQuery):
    await callback.answer()
