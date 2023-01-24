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
from keyboards.start import get_start_kb

router = Router()


@router.message(Command(commands=['help', 'start']))
async def help_cmd(message: Message):
    await message.answer(
        cf.HELP_MSG,
        reply_markup=get_start_kb()
    )
