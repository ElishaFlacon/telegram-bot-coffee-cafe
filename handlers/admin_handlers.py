from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from keyboards.admin_keyboard import *
from verification.admin_verify import *
from session.worker_session import *
from cash import *
from orders import *
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


#! =============================================================================================== !#


# Машина состояний для просмотра смены сотрудника
class FSMSessions(StatesGroup):
    name = State()
    date = State()
    days = State()


# Машина состояний для изменения сотрудника
class FSMWorkers(StatesGroup):
    option = State()
    worker_id = State()
    worker_name = State()


#! =============================================================================================== !#


# Команда открытия меню сотрудники
# * @dp.message_handler(commands=['Сотрудники'])
async def open_workers_menu(message: types.Message):
    try:
        if admin_verify(message.from_user.id) == True:
            await message.answer(f'Вы вошли в меню Сотрудники,\nВыберете необходимую команду', reply_markup=kb_admin_workers_menu)
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nПроверте консоль сервера на ошибки!\nНапишите команду ОТМЕНА!', reply_markup=kb_admin_cancel)
        print(f'admin_handlers Строка №38 - {e}')


# Команда открытия меню продукты
# * @dp.message_handler(commands=['Продукты'])
async def open_products_menu(message: types.Message):
    try:
        if admin_verify(message.from_user.id) == True:
            await message.answer(f'Вы вошли в меню Продукты,\nВыберете необходимую команду', reply_markup=kb_admin_products_menu)
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nПроверте консоль сервера на ошибки!\nНапишите команду ОТМЕНА!', reply_markup=kb_admin_cancel)
        print(f'admin_handlers Строка №49 - {e}')


# Команда открытия меню касса
# * @dp.message_handler(commands=['Касса'])
async def open_cash_menu(message: types.Message):
    try:
        if admin_verify(message.from_user.id) == True:
            await message.answer(f'Вы вошли в меню Касса,\nВыберете необходимую команду', reply_markup=kb_admin_cash_menu)
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nПроверте консоль сервера на ошибки!\nНапишите команду ОТМЕНА!', reply_markup=kb_admin_cancel)
        print(f'admin_handlers Строка №60 - {e}')


#! =============================================================================================== !#


# Команда для возвращения в основное меню
# * @dp.message_handler(Text(equals='НАЗАД', ignore_case=True), state='*')
async def back_main_menu(message: types.Message):
    try:
        if admin_verify(message.from_user.id) == True:
            await message.answer(f'Команда НАЗАД!,\nВы вернулись в основное меню', reply_markup=kb_admin_main_menu)
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nПроверте консоль сервера на ошибки!\nНапишите команду ОТМЕНА!', reply_markup=kb_admin_cancel)
        print(f'admin_handlers Строка №71 - {e}')


# Команда выхода из машины состояния (выше всех команд стейт машин)
# * @dp.message_handler(Text(equals='ОТМЕНА', ignore_case=True), state='*')
async def fsm_exit(message: types.Message, state: FSMContext):
    try:
        if admin_verify(message.from_user.id) == True:
            current_state = await state.get_state()
            await state.finish()
            await message.answer('Команда ОТМЕНА!\nВы вернулись в основное меню', reply_markup=kb_admin_main_menu)
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nПроверте консоль сервера на ошибки!\nНапишите команду ОТМЕНА!', reply_markup=kb_admin_cancel)
        print(f'worker_handlers Строка №85 - {e}')


#! =============================================================================================== !#


# Команда просмотра смен сотрудников
# * @dp.message_handler(commands=['Смены_сотрудников'])
async def worker_sessions(message: types.Message):
    try:
        if admin_verify(message.from_user.id) == True:
            await FSMSessions.name.set()
            await message.answer(f'Введите имя сотрудника:', reply_markup=kb_admin_cancel)
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nПроверте консоль сервера на ошибки!\nНапишите команду ОТМЕНА!', reply_markup=kb_admin_cancel)
        print(f'admin_handlers Строка №38 - {e}')


# Команда записи имени
# * @dp.message_handler(state=FSMSessions.name)
async def select_worker(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMSessions.next()
        await message.answer(f'Запишите с какой даты нужно начать поиск\nПример: 01.01.2000', reply_markup=kb_admin_cancel)
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nПроверте консоль сервера на ошибки!\nНапишите команду ОТМЕНА!', reply_markup=kb_admin_cancel)
        print(f'admin_handlers Строка №108 - {e}')


# Команда для записи с какой даты мы находим смену
# * @dp.message_handler(state=FSMSessions.date)
async def select_date(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['date'] = message.text
        await FSMSessions.next()
        await message.answer(f'Запишите количество дней\nПояснение: Если вам нужно найти смены сотрудника с 01.01.2000 до 10.01.2000, то вам нужно написать 9 дней', reply_markup=kb_admin_cancel)
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nПроверте консоль сервера на ошибки!\nНапишите команду ОТМЕНА!', reply_markup=kb_admin_cancel)
        print(f'admin_handlers Строка №108 - {e}')


# Команда для записи дней от той даты (то есть если от 1.09 нам нужно 7 дней, то будем искать с 1.09 до 8.09)
# * @dp.message_handler(state=FSMSessions.days)
async def select_quantity_days(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['days'] = message.text
        await FSMSessions.next()
        await message.answer(f'Ожидайте...', reply_markup=kb_admin_workers_menu)
        # !
        # ! И вот сюда пихаем поиск по сменам
        # !
        await state.finish()
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nПроверте консоль сервера на ошибки!\nНапишите команду ОТМЕНА!', reply_markup=kb_admin_cancel)
        print(f'admin_handlers Строка №108 - {e}')


#! =============================================================================================== !#


# Команда просмотра кто из сотрудников находится на смене в данный момент
# * @dp.message_handler(commands=['Активные_смены'])
async def active_sessions(message: types.Message):
    try:
        if admin_verify(message.from_user.id) == True:
            cas = check_active_sessions()
            if cas == '':
                await message.answer(f'Активных смен нет!', reply_markup=kb_admin_workers_menu)
            elif cas != '':
                await message.answer(f'Активные смены сотрудников:\n{cas}', reply_markup=kb_admin_workers_menu)
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nПроверте консоль сервера на ошибки!\nНапишите команду ОТМЕНА!', reply_markup=kb_admin_cancel)
        print(f'admin_handlers Строка №108 - {e}')


#! =============================================================================================== !#


# Команда добавления сотрудника
# * @dp.message_handler(commands=['Изменить_список_сотрудников'])
async def change_workers(message: types.Message):
    try:
        if admin_verify(message.from_user.id) == True:
            await FSMWorkers.option.set()
            await message.answer(f'Выберете действие:', reply_markup=kb_admin_worker_change_menu)
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nПроверте консоль сервера на ошибки!\nНапишите команду ОТМЕНА!', reply_markup=kb_admin_cancel)
        print(f'admin_handlers Строка №123 - {e}')


# Команда выбора опции (удалить, добавить)
# * @dp.message_handler(state=FSMWorkers.option)
async def select_option(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['option'] = message.text
        await FSMWorkers.next()
        if data['option'] == 'Добавить':
            await message.answer(f'Запишите айди', reply_markup=kb_admin_cancel)
        elif data['option'] == 'Удалить':
            await message.answer(f'Запишите айди', reply_markup=kb_admin_cancel)
        else:
            await message.answer(f'Такой команды нет!', reply_markup=kb_admin_cancel)
            await state.finish()
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nПроверте консоль сервера на ошибки!\nНапишите команду ОТМЕНА!', reply_markup=kb_admin_cancel)
        print(f'admin_handlers Строка №108 - {e}')


# Команда для записи айди работника
# * @dp.message_handler(state=FSMWorkers.worker_id)
async def select_worker_id(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['worker_id'] = message.text
        await FSMWorkers.next()
        await message.answer(f'Запишите имя', reply_markup=kb_admin_cancel)
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nПроверте консоль сервера на ошибки!\nНапишите команду ОТМЕНА!', reply_markup=kb_admin_cancel)
        print(f'admin_handlers Строка №108 - {e}')


# Команда для записи имени работника
# * @dp.message_handler(state=FSMWorkers.worker_name)
async def select_worker_name(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['worker_name'] = message.text
        change_workers_sheet(data['worker_name'],
                             data['worker_id'], data['option'])
        await state.finish()
        if data['option'] == 'Добавить':
            await message.answer(f'Сотрудник добавлен', reply_markup=kb_admin_main_menu)
        elif data['option'] == 'Удалить':
            await message.answer(f'Сотрудник удален', reply_markup=kb_admin_main_menu)
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nПроверте консоль сервера на ошибки!\nНапишите команду ОТМЕНА!', reply_markup=kb_admin_cancel)
        print(f'admin_handlers Строка №108 - {e}')


#! =============================================================================================== !#


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
        dp.register_message_handler(
            worker_sessions, commands=['Смены_сотрудников'])
        dp.register_message_handler(select_worker, state=FSMSessions.name)
        dp.register_message_handler(select_date, state=FSMSessions.date)
        dp.register_message_handler(
            select_quantity_days, state=FSMSessions.days)
        dp.register_message_handler(
            active_sessions, commands=['Активные_смены'])
        dp.register_message_handler(change_workers, commands=[
                                    'Изменить_список_сотрудников'])
        dp.register_message_handler(select_option, state=FSMWorkers.option)
        dp.register_message_handler(
            select_worker_id, state=FSMWorkers.worker_id)
        dp.register_message_handler(
            select_worker_name, state=FSMWorkers.worker_name)
    except Exception as e:
        print(f'admin_handlers ОШИБКА РЕГИСТРАЦИИ ХЕНДЛЕРОВ - {e}')
