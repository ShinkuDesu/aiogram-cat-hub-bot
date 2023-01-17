from api_key import TOKEN_API_KEY
import config as cf
import aiogram as am
import random
import string


bot = am.Bot(TOKEN_API_KEY)
dp = am.Dispatcher(bot)


ikb = am.types.InlineKeyboardMarkup()
more_ibtn = am.types.InlineKeyboardButton(
    text='Give me more!',
    callback_data='more cats',
)
recat_ibtn = am.types.InlineKeyboardButton(
    text='Reload cat',
    callback_data='reload cat',
)
save_ibtn = am.types.InlineKeyboardButton(
    text='Save cat',
    callback_data='save cat',
)
ikb.add(more_ibtn).add(recat_ibtn).add(save_ibtn)


@dp.message_handler(commands=['help', 'start'])
async def help_cmd(message: am.types.Message):
    kb = am.types.ReplyKeyboardMarkup(
    resize_keyboard=True,
    )
    cat_btn = am.types.KeyboardButton('/cat')
    advice_btn = am.types.KeyboardButton('/advice')
    kb.add(cat_btn).add(advice_btn)
    await message.answer(cf.HELP_MSG, reply_markup=kb)


@dp.message_handler(commands=['reply'])
async def reply_cmd(message: am.types.Message):
    await message.reply(text=message.text.replace('/reply', ''))


@dp.message_handler(commands=['answer'])
async def answer_cmd(message: am.types.Message):
    await message.answer(text=message.text.replace('/answer', ''))


@dp.message_handler(commands=['delete'])
async def delete_cmd(message: am.types.Message):
    await message.delete()


@dp.message_handler(commands=['advice'])
async def advice_cmd(message: am.types.Message):
    await message.answer(random.choice(cf.ADVICES))
    await message.delete()


@dp.message_handler(commands=['cat'])
async def cat_cmd(message: am.types.Message):
    print('cat send')
    
    await message.answer_photo(
        random.choice(cf.CATS_IMGS),
        reply_markup=ikb,
        caption=random.choice(cf.LMAO)
    )

@dp.callback_query_handler()
async def more_cats(callback: am.types.CallbackQuery):
    if callback.data == 'more cats':
        await cat_cmd(callback.message)
    if callback.data == 'reload cat':
        print('reload cat')
        photo = am.types.InputMediaPhoto(
            media=random.choice(cf.CATS_IMGS),
            type='photo',
            caption=random.choice(cf.LMAO),
        )
        await callback.message.edit_media(
            media=photo,
            reply_markup=ikb,
        )
    if callback.data == 'save cat':
        print('cat saved')
        await callback.message.delete_reply_markup()


@dp.message_handler(commands=['random'])
async def random_cmd(message: am.types.Message):
    try:
        msg = ''.join(random.choices(string.ascii_letters, k=int(message.text.replace('/random', ''))))
        await message.answer(msg)
    except:
        await message.reply('"' + message.text.replace('/random ', '') + '" is not a valid integer')


@dp.message_handler()
async def echo(message: am.types.Message):
    await message.answer(text=message.text)

async def on_startup(_):
    print('Bot is running')

if __name__ == '__main__':
    am.executor.start_polling(
        dp,
        on_startup=on_startup,
        skip_updates=True,
    )
