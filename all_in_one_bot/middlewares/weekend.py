from datetime import datetime
from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.flags import get_flag
from aiogram.utils.chat_action import ChatActionSender

def _is_weekend() -> bool:
    return datetime.utcnow().weekday() in (5, 6)


class WeekendMessageMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        if not _is_weekend():
            return await handler(event, data)


class WeekendCallbackMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[CallbackQuery, Dict[str, Any]], Awaitable[Any]],
        event: CallbackQuery,
        data: Dict[str, Any]
    ) -> Any:
        if not _is_weekend():
            return await handler(event, data)

        await event.answer(
            "Бот по выходным не работает!",
            show_alert=True
        )
        return



class ChatActionMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        upload_photo = get_flag(data, "upload_photo")

        if not upload_photo:
            return await handler(event, data)

        async with ChatActionSender.upload_photo(chat_id=event.chat.id):
            return await handler(event, data)
