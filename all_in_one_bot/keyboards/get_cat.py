from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.filters.callback_data import CallbackData
from typing import Optional


class CatsCallbackFactory(CallbackData, prefix='cats'):
    action: str
    value: Optional[int]


def get_cats_ikb():
    Cats_ikb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='👍',
                    callback_data=CatsCallbackFactory(action='like', value=+1).pack(),
                ),
                InlineKeyboardButton(
                text='Give me more!',
                callback_data=CatsCallbackFactory(action='more_cats', value=+1).pack(),
                ),
                InlineKeyboardButton(
                    text='👎',
                    callback_data=CatsCallbackFactory(action='like', value=-1).pack(),
                )
            ],
        ]
    )
    return Cats_ikb