from api_key import TOKEN_API_KEY
import config as cf
import aiogram as am
import random
import string


bot = am.Bot(TOKEN_API_KEY)
dp = am.Dispatcher(bot)


kb = am.types.ReplyKeyboardMarkup(
    resize_keyboard=True,
)
cat_btn = am.types.KeyboardButton('/cat')
advice_btn = am.types.KeyboardButton('/advice')
kb.add()



@dp.message_handler(commands=['help', 'start'])
async def help_cmd(message: am.types.Message):
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


@dp.message_handler(commands=['adwice'])
async def advice_cmd(message: am.types.Message):
    await message.answer(random.choice(cf.ADVICES))
    await message.delete()


@dp.message_handler(commands=['cat'])
async def cat_cmd(message: am.types.Message):
    await message.answer_photo(random.choice(cf.CATS_IMGS))
    await message.delete()


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
