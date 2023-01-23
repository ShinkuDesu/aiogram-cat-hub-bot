from typing import List

from aiogram import Router
from aiogram import F
from aiogram.types import Message

from filters.find_usernames import HasUsernamesFilter

router = Router()


@router.message(
    F.text,
    HasUsernamesFilter(),
)
async def message_with_usernames(
        message: Message,
        usernames: List[str]
):
    await message.answer(
        f'Спасибо! Обязательно подпишусь на '
        f'{", ".join(usernames)}'
    )
