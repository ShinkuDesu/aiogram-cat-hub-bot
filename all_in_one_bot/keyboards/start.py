from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
)


def get_start_kb():
    start_kb = ReplyKeyboardMarkup(
            keyboard=[
                [KeyboardButton(text='/cat'),
                KeyboardButton(text='/advice')]
            ],
            one_time_keyboard=True,
            resize_keyboard=True,
            input_field_placeholder='Шо делать?',
        )
    return start_kb
