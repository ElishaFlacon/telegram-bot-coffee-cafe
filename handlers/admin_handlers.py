from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from keyboards.admin_keyboard import *
from verification.admin_verify import *
from session.worker_session import *
from cash import *
from orders import *
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


# Команда открытия меню сотрудники
# * @dp.message_handler(commands=['Сотрудники'])
async def open_workers_menu(message: types.Message):
    try:
        if admin_verify(message.from_user.id) == True:
            await message.answer(f'Вы вошли в меню Сотрудники,\nВыберете необходимую команду', reply_markup=kb_admin_workers_menu)
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nПроверте консоль сервера на ошибки!')
        print(f'admin_handlers Строка №38 - {e}')


# Команда открытия меню продукты
# * @dp.message_handler(commands=['Продукты'])
async def open_products_menu(message: types.Message):
    try:
        if admin_verify(message.from_user.id) == True:
            await message.answer(f'Вы вошли в меню Продукты,\nВыберете необходимую команду', reply_markup=kb_admin_products_menu)
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nПроверте консоль сервера на ошибки!')
        print(f'admin_handlers Строка №49 - {e}')


# Команда открытия меню касса
# * @dp.message_handler(commands=['Касса'])
async def open_cash_menu(message: types.Message):
    try:
        if admin_verify(message.from_user.id) == True:
            await message.answer(f'Вы вошли в меню Касса,\nВыберете необходимую команду', reply_markup=kb_admin_cash_menu)
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nПроверте консоль сервера на ошибки!')
        print(f'admin_handlers Строка №60 - {e}')


# Команда для возвращения в основное меню
# * @dp.message_handler(Text(equals='НАЗАД', ignore_case=True), state='*')
async def back_main_menu(message: types.Message):
    try:
        if admin_verify(message.from_user.id) == True:
            await message.answer(f'Команда Назад,\nВы вернулись в основное меню', reply_markup=kb_admin_main_menu)
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nПроверте консоль сервера на ошибки!')
        print(f'admin_handlers Строка №71 - {e}')


# Команда выхода из машины состояния (выше всех команд стейт машин)
# * @dp.message_handler(Text(equals='ОТМЕНА', ignore_case=True), state='*')
async def fsm_exit(message: types.Message, state: FSMContext):
    try:
        if admin_verify(message.from_user.id) == True:
            current_state = await state.get_state()
            if current_state is None:
                return
            await state.finish()
            await message.answer('ОТМЕНА!', reply_markup=kb_admin_main_menu)
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nПроверте консоль сервера на ошибки!')
        print(f'worker_handlers Строка №85 - {e}')


# Команда просмотра смен сотрудников
# * @dp.message_handler(commands=['Смены_сотрудников'])
async def open_workers_menu(message: types.Message):
    try:
        if admin_verify(message.from_user.id) == True:
            await message.answer(f'', reply_markup=kb_admin_workers_menu)
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nПроверте консоль сервера на ошибки!')
        print(f'admin_handlers Строка №38 - {e}')


# Команда просмотра кто из сотрудников находится на смене в данный момент
# * @dp.message_handler(commands=['Кто_на_смене'])
async def open_workers_menu(message: types.Message):
    try:
        if admin_verify(message.from_user.id) == True:
            await message.answer(f'', reply_markup=kb_admin_workers_menu)
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nПроверте консоль сервера на ошибки!')
        print(f'admin_handlers Строка №38 - {e}')


# Команда добавления сотрудника
# * @dp.message_handler(commands=['Добавить_сотрудника'])
async def open_workers_menu(message: types.Message):
    try:
        if admin_verify(message.from_user.id) == True:
            await message.answer(f'', reply_markup=kb_admin_workers_menu)
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nПроверте консоль сервера на ошибки!')
        print(f'admin_handlers Строка №38 - {e}')


# Команда удаления сотрудника
# * @dp.message_handler(commands=['Удалить_сотрудника'])
async def open_workers_menu(message: types.Message):
    try:
        if admin_verify(message.from_user.id) == True:
            await message.answer(f'', reply_markup=kb_admin_workers_menu)
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nПроверте консоль сервера на ошибки!')
        print(f'admin_handlers Строка №38 - {e}')


#! Регистрация всех хендлеров
def register_admin_handlers(dp: Dispatcher):
    try:
        dp.register_message_handler(open_workers_menu, commands=['Сотрудники'])
        dp.register_message_handler(open_products_menu, commands=['Продукты'])
        dp.register_message_handler(open_cash_menu, commands=['Касса'])
        dp.register_message_handler(back_main_menu, Text(
            equals='НАЗАД', ignore_case=True), state='*')
        dp.register_message_handler(fsm_exit, Text(
            equals='ОТМЕНА', ignore_case=True), state='*')
    except Exception as e:
        print(f'admin_handlers ОШИБКА РЕГИСТРАЦИИ ХЕНДЛЕРОВ - {e}')
