from aiogram import Bot, Dispatcher, executor, types
import logging
from aiogram.types import ReplyKeyboardRemove
from keys import API_TOKEN
from keyboards import *
from verification import *
from session import *
from orders import *


def on_startup():
    print('БОТ ЗАПУЩЕН!!!')


# ЛОГИНИМСЯ
logging.basicConfig(level=logging.INFO)

# ИНИЦИАЛИЗИРУЕМ БОТА И ДИСПЕТЧЕРА
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# Команда старта
@dp.message_handler(commands=['start'])
async def start_working(message: types.Message):
    if admin_vefify(message.from_user.id) == True:
        await message.answer(f'Здравствуйте, {message.from_user.full_name}, вы АДМИН!', reply_markup=None)
    elif worker_vefify(message.from_user.id) == True:
        await message.answer(f'Здравствуйте, {message.from_user.full_name}, вы хотиет начать смену?', reply_markup=kb_worker_start_session)
    else:
        await message.answer(f'Здравствуйте, вы гей!')


# Команда начала смены
@dp.message_handler(commands=['Начать_смену'])
async def start_session(message: types.Message):
    # Если у мужика смена не начата
    if worker_vefify(message.from_user.id) == True and worker_session_status(message.from_user.id) == False:
        worker_start_session(message.from_user.id)
        await message.answer(f'{message.from_user.full_name}, Вы начали смену!', reply_markup=kb_worker_main_menu)
    # Если у мужика смена уже начата
    elif worker_vefify(message.from_user.id) == True and worker_session_status(message.from_user.id) == True:
        await message.answer(f'{message.from_user.full_name}, Завершите прошлую смену, чтобы начать новую смену', reply_markup=kb_worker_end_session)


# Команда создания заказа
@dp.message_handler(commands=['Создать_заказ'])
async def create_order(message: types.Message):
    if worker_vefify(message.from_user.id) == True and worker_session_status(message.from_user.id) == True:
        await message.answer(f'Вы начали собирать заказ {create_new_order(message.from_user.id)}', reply_markup=kb_worker_create_order)


# Команда добавления продукта
@dp.message_handler(commands=['Добавить'])
async def add_product_to_order(message: types.Message):
    if worker_vefify(message.from_user.id) == True and worker_session_status(message.from_user.id) == True:
        append_product_to_order(get_product(
            message.text), get_count_being_created_order(message.from_user.id))
        await message.answer(f'Вы добавили в заказ №{get_count_being_created_order(message.from_user.id)}: <strong>{get_product(message.text)}</strong>', parse_mode='html')


# Команда завершения создания заказа
@dp.message_handler(commands=['Завершить_создание_заказа'])
async def complete_creating_order(message: types.Message):
    if worker_vefify(message.from_user.id) == True and worker_session_status(message.from_user.id) == True:
        await message.answer(f'Вы завершили создание заказа №{get_count_being_created_order(message.from_user.id)}: <strong>{get_all_products(get_count_being_created_order(message.from_user.id))}</strong>', parse_mode='html', reply_markup=kb_worker_main_menu)
        complete_create_order(
            get_count_being_created_order(message.from_user.id))


# Команда просмотра текущих заказов
@dp.message_handler(commands=['Текущие_заказы'])
async def check_actua_orders(message: types.Message):
    if worker_vefify(message.from_user.id) == True and worker_session_status(message.from_user.id) == True:
        for i in range(get_count_all_orders()):
            # Зачем i+1? чтобы верхняя строка не попадала, иначе выведет None
            await message.answer(f'{check_running_orders(i+1)}', parse_mode='html', reply_markup=create_inline_keyboard(i+1))


# Тут будут все команды от инлайн кнопок
@dp.callback_query_handler()
async def inline_keyboards_commands(callback: types.CallbackQuery):
    if callback.data.split()[0] == '++':
        await callback.answer(f'Выполняем заказ {callback.data}')
    elif callback.data.split()[0] == '--':
        await callback.answer(f'Удаляем заказ {callback.data}')


# Команда закрытия смены
@dp.message_handler(commands=['Закрыть_смену'])
async def end_session(message: types.Message):
    # Если у мужика смена открыта
    if worker_vefify(message.from_user.id) == True and worker_session_status(message.from_user.id) == True:
        worker_end_session(message.from_user.id)
        await message.answer(f'{message.from_user.full_name}, Закрыл вашу смену', reply_markup=ReplyKeyboardRemove())
    # Если у мужика смена уже закрыта
    elif worker_vefify(message.from_user.id) == True and worker_session_status(message.from_user.id) == False:
        await message.answer(f'<strong>Вы уже закрыли смену!</strong>\nЕсли вы не закрывали смену, обратитесь к Администратору!', reply_markup=ReplyKeyboardRemove(), parse_mode='html')


# ЗАПУСК
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup())
