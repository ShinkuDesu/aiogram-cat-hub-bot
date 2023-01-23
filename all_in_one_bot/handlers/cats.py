import random
import time

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
from keyboards import cats
from configs import config as cf


router = Router()


@router.message(
    Command(commands=['cat']),
    flags={"upload_photo": "upload_cat"}
)
async def cat_cmd(message: Message):
    print('cat send')
    time.sleep(1)
    await message.answer_photo(
        random.choice(cf.CATS_IMGS),
        reply_markup=cats.get_cats_ikb(),
        caption=random.choice(cf.LMAO)
    )


@router.callback_query(
    F.data == 'more cats',
)
async def more_cats(callback: CallbackQuery):
    await cat_cmd(callback.message)
    await callback.answer()


@router.callback_query(
    F.data == 'reload cat',
)
async def reload_cat(callback: CallbackQuery):
    print('reload cat')
    photo = InputMediaPhoto(
        media=random.choice(cf.CATS_IMGS),
        type='photo',
        caption=random.choice(cf.LMAO),
    )
    await callback.message.edit_media(
        media=photo,
        reply_markup=cats.get_cats_ikb(),
    )
    await callback.answer()

@router.callback_query(
    F.data == 'save cat',
)
async def save_cats(callback: CallbackQuery):
    await callback.answer()
    print('cat saved')
    await callback.message.delete_reply_markup()
