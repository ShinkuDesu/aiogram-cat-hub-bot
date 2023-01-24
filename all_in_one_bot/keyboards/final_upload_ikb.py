from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.filters.callback_data import CallbackData


class FinalUploadCallbackFactory(CallbackData, prefix='upload_cats'):
    action: str


def get_final_upload_ikb():
    final_upload_ikb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Все верно',
                    callback_data=FinalUploadCallbackFactory(action='correctly').pack(),
                ),
                InlineKeyboardButton(
                    text='Все не верно',
                    callback_data=FinalUploadCallbackFactory(action='incorrectly').pack(),
                )
            ],
        ]
    )
    return final_upload_ikb
