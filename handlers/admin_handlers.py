from aiogram import types, Dispatcher
from keyboards import *
from verification import *
from create import dp


#! Регистрация всех хендлеров
def register_admin_handlers(dp: Dispatcher):
    try:
        pass
    except Exception as e:
        print(f'admin_handlers ОШИБКА РЕГИСТРАЦИИ ХЕНДЛЕРОВ - {e}')
