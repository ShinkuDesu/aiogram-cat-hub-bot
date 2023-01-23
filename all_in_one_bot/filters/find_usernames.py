from typing import Union, Dict, Any

from aiogram.filters import Filter
from aiogram.types import Message


class HasUsernamesFilter(Filter):
    async def __call__(self, message: Message) -> Union[bool, Dict[str, Any]]:
        entities = message.entities or []

        found_usernames = [
            item.extract_from(message.text) for item in entities
            if item.type == "mention"
        ]

        if len(found_usernames) > 0:
            return {"usernames": found_usernames}
        return False
