import asyncio
import logging
import os
import sys

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from notion_bot.handlers import common_router

logger = logging.getLogger(__name__)


def _configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )


async def main() -> None:
    load_dotenv()
    token = os.getenv("BOT_TOKEN", "").strip()
    if not token:
        logger.error("Задайте переменную окружения BOT_TOKEN (см. .env.example).")
        sys.exit(1)

    _configure_logging()
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_router(common_router)

    logger.info("Запуск polling…")
    await dp.start_polling(bot)


def run() -> None:
    asyncio.run(main())


if __name__ == "__main__":
    run()
