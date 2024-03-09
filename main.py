import asyncio
import logging
from bot import bot, dp
from handlers.start import start_router
from handlers.pic import pic_router
from handlers.echo import echo_router


async def main():
    # Регитсрация роутеров
    dp.include_router(pic_router)
    dp.include_router(start_router)
    dp.include_router(echo_router)
    # запуск бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())