import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from config_data.config import PROXY, BOT_TOKEN


async def start():

    session = AiohttpSession(
        proxy=PROXY
    )

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )

    bot = Bot(token=BOT_TOKEN,
              session=session,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(storage=MemoryStorage())

    try:
        me = await bot.me()
        print(f"Бот запущен: @{me.username} (id: {me.id})")
        print("Polling запущен...")
        await dp.start_polling(bot)
    except Exception as e:
        logging.error(f"Не удалось запустить бота: {e}")
        sys.exit(1)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(start())
    except KeyboardInterrupt:
        print("Бот остановлен вручную")