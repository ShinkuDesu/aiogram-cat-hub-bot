from aiogram import Router, Bot
from aiogram.filters.command import Command
from aiogram.types import Message

router = Router()


@router.message(Command(commands=["ban"]))
async def cmd_ban(message: Message, admins: set[int], bot: Bot):
    if message.from_user.id not in admins:
        await message.answer(
            "У вас недостаточно прав для совершения этого действия"
        )
    else:
        await bot.ban_chat_member(
            chat_id=message.chat.id,
            user_id=message.reply_to_message.from_user.id
        )
        await message.answer("Нарушитель заблокирован")
