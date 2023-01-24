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
    InputMediaPhoto,
)
from keyboards.cats import get_cats_ikb, CatsCallbackFactory
from configs import config as cf


router = Router()


@router.message(
    Command(commands=['cat']),
    flags={"upload_photo": "upload_cat"}
)
async def cat_cmd(message: Message):
    await message.answer_photo(
        random.choice(cf.CATS_IMGS),
        reply_markup=get_cats_ikb(),
        caption=random.choice(cf.LMAO)
    )

@router.message(
    Command(commands=['upload'])
)
async def upload_cmd(message: Message):
    await message.answer(
        text='Загрузите картинку котика'
    )


@router.callback_query(
    CatsCallbackFactory.filter(F.action=='more_cats')
)
async def more_cats_fab(callback: CallbackQuery):
    await cat_cmd(callback.message)
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
