from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)


def get_cats_ikb():
    Cats_ikb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Reload cat',
                    callback_data='reload cat',
                ),
                InlineKeyboardButton(
                    text='Save cat',
                    callback_data='save cat',
                )
            ],
            [
                InlineKeyboardButton(
                text='Give me more!',
                callback_data='more cats',
                ),
            ],
            
        ]
    )
    return Cats_ikb


