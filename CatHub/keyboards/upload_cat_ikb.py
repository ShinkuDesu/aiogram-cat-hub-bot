from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    Message
)
from aiogram.filters.callback_data import CallbackData
from typing import Optional

class UploadCallbackFactory(CallbackData, prefix='upload_cats'):
    action: str


def get_final_upload_ikb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Все верно',
                    callback_data=UploadCallbackFactory(action='correctly').pack(),
                ),
                InlineKeyboardButton(
                    text='Все не верно',
                    callback_data=UploadCallbackFactory(action='cancel').pack(),
                )
            ],
        ]
    )

def get_cancel_ikb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='Отменить загрузку',
                    callback_data=UploadCallbackFactory(action='cancel').pack(),
                ),
            ]
        ]
    )

def get_admin_ikb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text='В партию!',
                    callback_data=UploadCallbackFactory(action='approved').pack(),
                ),
                InlineKeyboardButton(
                    text='Гнать его!',
                    callback_data=UploadCallbackFactory(action='reject').pack(),
                ),
            ]
        ]
    )
