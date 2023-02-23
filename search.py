import pandas as pd
from random import randint
from config import token
from aiogram import Dispatcher, Bot, executor, types

bot = Bot(token=token)
dp = Dispatcher(bot)

movie_json = pd.read_json("/Users/Bogruk/imdb_scrap/result_1.json")

def choose_movie():
    m_index = randint(0, len(movie_json))
    return m_index

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    # keyboard = types.ReplyKeyboardMarkup("random movie")
    await message.reply(f"you can watch: {movie_json.loc[choose_movie()]}")


if __name__ == "__main__":
    # choose_movie()
    executor.start_polling(dp, skip_updates=True)


print(movie_json.loc[choose_movie()])

