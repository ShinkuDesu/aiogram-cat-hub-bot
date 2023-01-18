from aiogram.types import (
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    KeyboardButton,
)
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

start_kb = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text='/cat'),
            KeyboardButton(text='/advice')]
        ],
        one_time_keyboard=True,
        resize_keyboard=True,
        input_field_placeholder='Шо делать?',
    )
