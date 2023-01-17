import aiogram
from api_key import TOKEN_API_KEY


bot = aiogram.Bot(TOKEN_API_KEY)
dp = aiogram.Dispatcher(bot)
