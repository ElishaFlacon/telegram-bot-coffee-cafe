from unicodedata import name
from aiogram import types, Dispatcher
from keyboards.admin_keyboard import *
from verification.admin_verify import *
from cash import *
from orders import *
from create import dp
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


# Машина состояний для просмотра смены сотрудника
class FSMProducts(StatesGroup):
    name = State()
    first_date = State()
    second_date = State()


# Машина состояний для добавления сотрудника
class FSMProducts(StatesGroup):
    worker_id = State()
    name = State()


# Машина состояний для удаления сотрудника
class FSMProducts(StatesGroup):
    worker_id = State()


#! Регистрация всех хендлеров
def register_admin_handlers(dp: Dispatcher):
    try:
        pass
    except Exception as e:
        print(f'admin_handlers ОШИБКА РЕГИСТРАЦИИ ХЕНДЛЕРОВ - {e}')
