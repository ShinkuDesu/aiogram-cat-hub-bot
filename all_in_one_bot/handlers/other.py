from aiogram import (
    Router,
)
from aiogram.filters import (
    Text,
)
from aiogram.types import (
    Message,
)

router = Router()


@router.message(Text('text'))
async def help_cmd(message: Message):
    await message.answer(message.text) # type: ignore
