from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import logging
from aiogram.types import ReplyKeyboardRemove
from keys import API_TOKEN
from keyboards import *
from verification import *
from session import *
from orders import *
# для стейт машины
from aiogram.contrib.fsm_storage.memory import MemoryStorage
# для хендлеров
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMProducts(StatesGroup):
    product = State()
    taste = State()
    additions = State()
    topping = State()


def on_startup():
    print('БОТ ЗАПУЩЕН!!!')


# Память
storage = MemoryStorage()

# ЛОГИНИМСЯ
logging.basicConfig(level=logging.INFO)

# ИНИЦИАЛИЗИРУЕМ БОТА И ДИСПЕТЧЕРА
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)


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
@dp.message_handler(commands=['Добавить_продукт'])
async def add_product_to_order(message: types.Message):
    if worker_vefify(message.from_user.id) == True and worker_session_status(message.from_user.id) == True:
        await FSMProducts.product.set()
        await message.answer('Выберите продукт', reply_markup=kb_worker_append_product)


# Выход из машины состояния, команда отмены (выше всех команд добавления продуктов)
@dp.message_handler(Text(equals='ОТМЕНА', ignore_case=True), state='*')
async def cancel_selected(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer('ОТМЕНА!', reply_markup=kb_worker_create_order)


# Выбор продукта
@dp.message_handler(state=FSMProducts.product)
async def select_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product'] = message.text
    await FSMProducts.next()
    if data['product'] == 'Мороженое':
        await message.answer('Выберите вкус мороженого', reply_markup=kb_worker_select_taste_icecream)
    elif data['product'] == 'Чай':
        await message.answer('Выберите вкус чая', reply_markup=kb_worker_select_taste_tea)
    elif data['product'] == 'Лимонад':
        await message.answer('Выберите вкус лимонада', reply_markup=kb_worker_select_taste_lemonade)
    elif data['product'] == 'Смузи':
        await message.answer('Выберите вкус смузи', reply_markup=kb_worker_select_taste_smoothie)
    elif data['product'] == 'Вафля':
        append_product_to_order(get_dict_items(
            data), get_number_being_created_order(message.from_user.id))
        await message.answer(f'Заказ №{get_number_being_created_order(message.from_user.id)}: {get_all_products(get_number_being_created_order(message.from_user.id))}', reply_markup=kb_worker_create_order)
        await state.finish()
    elif data['product'] == 'Молочный_коктель':
        await message.answer('Выберите вкус молчного коктеля', reply_markup=kb_worker_select_taste_milkshake)
    else:
        await message.answer('Такого продукта нет!', reply_markup=kb_worker_create_order)
        await state.finish()


# Выбор вкуса продукта
@dp.message_handler(state=FSMProducts.taste)
async def select_taste(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['taste'] = message.text
    # Проверка на мороженное чтобы в дальшнейшем мы смогли добавить топинги
    if data['product'] == 'Мороженое':
        await message.answer('Выберите посыпку для мороженного', reply_markup=kb_worker_select_additions_icecream)
        await FSMProducts.next()
        # Задаем значение для посыпки
        # Чтобы можно было нормально записать сразу несколько посыпок
        # Иначе я не придумал
        async with state.proxy() as data:
            data['additions'] = ''
    else:
        async with state.proxy() as data:
            append_product_to_order(get_dict_items(
                data), get_number_being_created_order(message.from_user.id))
            await message.answer(f'Заказ №{get_number_being_created_order(message.from_user.id)}: {get_all_products(get_number_being_created_order(message.from_user.id))}',  reply_markup=kb_worker_create_order)
        await state.finish()


# Выбор посыпки для мороженного
@dp.message_handler(state=FSMProducts.additions)
async def select_toping(message: types.Message, state: FSMContext):
    if message.text == 'Завершить':
        await FSMProducts.next()
        await message.answer('Выберите топинг для мороженного', reply_markup=kb_worker_select_topping_icecream)
    elif message.text == 'Без_Посыпки':
        async with state.proxy() as data:
            data['additions'] = f'{message.text} '
        await FSMProducts.next()
        await message.answer('Выберите топинг для мороженного', reply_markup=kb_worker_select_topping_icecream)
    else:
        async with state.proxy() as data:
            data['additions'] += f'{message.text} '
            await message.answer(f'Добавлена посыпка: {message.text}')


# Выбор топинга для мороженного
@dp.message_handler(state=FSMProducts.topping)
async def select_toping(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['toping'] = message.text
    async with state.proxy() as data:
        append_product_to_order(get_dict_items(
            data), get_number_being_created_order(message.from_user.id))
        await message.answer(f'Заказ №{get_number_being_created_order(message.from_user.id)}: {get_all_products(get_number_being_created_order(message.from_user.id))}',  reply_markup=kb_worker_create_order)
    await state.finish()


# Команда отмены заказа
@ dp.message_handler(commands=['Отменить_создание_заказа'])
async def complete_creating_order(message: types.Message):
    if worker_vefify(message.from_user.id) == True and worker_session_status(message.from_user.id) == True:
        await message.answer(f'Вы отменили создание заказа №{get_number_being_created_order(message.from_user.id)}. <strong>Заказ удален!</strong>', parse_mode='html', reply_markup=kb_worker_main_menu)
        remove_order(get_number_being_created_order(message.from_user.id))


# Команда завершения создания заказа
@ dp.message_handler(commands=['Завершить_создание_заказа'])
async def complete_creating_order(message: types.Message):
    if worker_vefify(message.from_user.id) == True and worker_session_status(message.from_user.id) == True:
        await message.answer(f'Вы завершили создание заказа №{get_number_being_created_order(message.from_user.id)}: <strong>{get_all_products(get_number_being_created_order(message.from_user.id))}Цена: {get_order_price(get_number_being_created_order(message.from_user.id))} Р.</strong> ', parse_mode='html', reply_markup=kb_worker_main_menu)
        load_order_price(get_order_price(get_number_being_created_order(
            message.from_user.id)), get_number_being_created_order(message.from_user.id))
        complete_create_order(
            get_number_being_created_order(message.from_user.id))


# Команда просмотра текущих заказов
@ dp.message_handler(commands=['Текущие_заказы'])
async def check_actua_orders(message: types.Message):
    if worker_vefify(message.from_user.id) == True and worker_session_status(message.from_user.id) == True:
        for i in range(get_count_all_orders()):
            # Зачем i+1? чтобы верхняя строка не попадала, иначе выведет None
            if check_running_orders(i+1) == True:
                await message.answer(f'Текущий Заказ №{i+1}: <strong>{get_all_products(i+1)} Цена: {get_order_price(i+1)} Р.</strong>', parse_mode='html', reply_markup=create_inline_keyboard(i+1))


# Команда просмотра завершенных заказов
@ dp.message_handler(commands=['Выполненные_заказы'])
async def check_actua_orders(message: types.Message):
    if worker_vefify(message.from_user.id) == True and worker_session_status(message.from_user.id) == True:
        for i in range(get_count_all_orders()):
            # Зачем i+1? чтобы верхняя строка не попадала, иначе выведет None
            if check_completed_orders(i+1) == True:
                await message.answer(f'Завершенный Заказ №{i+1}: <strong>{get_all_products(i+1)} Цена: {get_order_price(i+1)} Р.</strong>', parse_mode='html')


# Тут будут все команды от инлайн кнопок
@ dp.callback_query_handler()
async def inline_keyboards_commands(callback: types.CallbackQuery):
    if callback.data.split()[0] == '++':
        await callback.answer(f'🟩 Заказ №{callback.data.split()[1]} Завершен!')
        complete_order(callback.data.split()[1])
    elif callback.data.split()[0] == '--':
        await callback.answer(f'🟥 Заказ №{callback.data.split()[1]} Удален!')
        remove_order(callback.data.split()[1])


# Команда закрытия смены
@ dp.message_handler(commands=['Закрыть_смену'])
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
