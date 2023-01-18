import random

from aiogram import (
    Router,
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


@router.message(Command(commands=['cat']))
async def cat_cmd(message: Message):
    print('cat send')
    
    await message.answer_photo(
        random.choice(cf.CATS_IMGS),
        reply_markup=cats.get_cats_ikb(),
        caption=random.choice(cf.LMAO)
    )


@router.callback_query()
async def more_cats(callback: CallbackQuery):
    await callback.answer()
    if callback.data == 'more cats':
        await cat_cmd(callback.message)
    if callback.data == 'reload cat':
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
    if callback.data == 'save cat':
        print('cat saved')
        await callback.message.delete_reply_markup()
