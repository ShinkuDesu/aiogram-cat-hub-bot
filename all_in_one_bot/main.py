from api_key import TOKEN_API_KEY
import config as cf
import keyboads as kb
import random
import logging

from aiogram import (
    Bot,
    Dispatcher,
    types,
)
from aiogram.filters import (
    Command,
    Text,
)
from aiogram.types import (
    Message,
    CallbackQuery,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    InputMediaPhoto,
)

logger = logging.getLogger(__name__)
dp = Dispatcher()


@dp.message(Command(commands=['help', 'start']))
async def help_cmd(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, cf.HELP_MSG, reply_markup=kb.start_kb)


@dp.message(Command(commands=['reply']))
async def reply_cmd(message: Message):
    await message.reply(text=message.text)  # type: ignore


@dp.message(Command(commands=['answer']))
async def answer_cmd(message: Message):
    await message.answer(text=message.text) # type: ignore


@dp.message(Command(commands=['delete']))
async def delete_cmd(message: Message):
    await message.delete()


@dp.message(Command(commands=['advice']))
async def advice_cmd(message: Message):
    await message.answer(random.choice(cf.ADVICES))
    await message.delete()


@dp.message(Command(commands=['cat']))
async def cat_cmd(message: Message):
    print('cat send')
    
    await message.answer_photo(
        random.choice(cf.CATS_IMGS),
        reply_markup=kb.Cats_ikb,
        caption=random.choice(cf.LMAO)
    )

@dp.callback_query()
async def more_cats(callback: CallbackQuery):
    await callback.answer()
    if callback.data == 'more cats':
        await cat_cmd(callback.message)
    if callback.data == 'reload cat':
        print('reload cat')
        photo = InputMediaPhoto(
            media=random.choice(cf.CATS_IMGS),
            type='photo',
            caption=random.choice(cf.LMAO),
        )
        await callback.message.edit_media(
            media=photo,
            reply_markup=kb.Cats_ikb,
        )
    if callback.data == 'save cat':
        print('cat saved')
        await callback.message.delete_reply_markup()


@dp.message()
async def echo(message: Message):
    await message.send_copy(chat_id=message.chat.id)

async def on_startup(_):
    print('Bot is running')

def main() -> None:
    print('Starting')
    # Initialize Bot instance with an default parse mode which will be passed to all API calls
    bot = Bot(TOKEN_API_KEY, parse_mode="HTML")
    # And the run events dispatching
    dp.run_polling(
        bot
    )


if __name__ == "__main__":
    main()
