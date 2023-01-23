from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from filters.chat_type import ChatTypeFilter

router = Router()
# router.message.filter(F.chat.type.in_({"group", "supergroup"}))
router.message.filter(
    ChatTypeFilter(chat_type=["group", "supergroup"])
)


@router.message(
    Command(commands=["dice"]),
)
async def cmd_dice_in_group(message: Message):
    await message.answer_dice(emoji="🎲")


@router.message(
    Command(commands=["basketball"]),
)
async def cmd_basketball_in_group(message: Message):
    await message.answer_dice(emoji="🏀")
