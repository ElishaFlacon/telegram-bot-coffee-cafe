from aiogram import Bot, Dispatcher
import logging
from keys import API_TOKEN
from aiogram.contrib.fsm_storage.memory import MemoryStorage


# Логинимся, инициализируем бота и диспетчера и инициализируем память
try:
    storage = MemoryStorage()
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(bot, storage=storage)
except Exception as e:
    print(f'create ОШИБКА СОЗДАНИЯ БОТА - {e}')

