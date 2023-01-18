import random

from aiogram import (
    Bot,
    Router,
)
from aiogram.filters import (
    Command,
)
from aiogram.types import (
    Message,
)
from configs import config as cf
from keyboards import start, cats

router = Router()


@router.message(Command(commands=['help', 'start']))
async def help_cmd(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, cf.HELP_MSG, reply_markup=start.get_start_kb())


@router.message(Command(commands=['reply']))
async def reply_cmd(message: Message):
    await message.reply(text=message.text)  # type: ignore


@router.message(Command(commands=['answer']))
async def answer_cmd(message: Message):
    await message.answer(text=message.text) # type: ignore


@router.message(Command(commands=['delete']))
async def delete_cmd(message: Message):
    await message.delete()


@router.message(Command(commands=['advice']))
async def advice_cmd(message: Message):
    await message.answer(random.choice(cf.ADVICES))
    await message.delete()


@router.message(Command(commands=['cat']))
async def cat_cmd(message: Message):
    print('cat send')
    
    await message.answer_photo(
        random.choice(cf.CATS_IMGS),
        reply_markup=cats.get_cats_ikb(),
        caption=random.choice(cf.LMAO)
    )