from aiogram import (
    Router,
    F,
)
from aiogram.filters import (
    Text,
    Filter
)
from aiogram.types import (
    Message,
)

router = Router()

# F.content_type.in_({'text', 'sticker', 'photo'})
@router.message(F.text)
async def echo_text(message: Message):
    await message.answer(message.text) # type: ignore

@router.message(F.photo[-1].file_id.as_('photo_id'))
async def echo_img(message: Message, photo_id:str):
    await message.answer_photo(photo_id) # type: ignore
