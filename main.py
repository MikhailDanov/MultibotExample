import asyncio
from aiogram import Bot, Dispatcher, types


TOKENS = ['token1', 'tokenX']
bots = [Bot(token) for token in TOKENS]
dp = Dispatcher()


@dp.message()
async def send_echo_message(message: types.Message):
    bot = await message.bot.get_me()
    await message.answer(f"Это бот {bot.first_name}, вы написали \"{message.text}\"")


async def main():
    tasks = dp.start_polling(*bots)
    await asyncio.gather(tasks)


if __name__ == '__main__':
    asyncio.run(main())
