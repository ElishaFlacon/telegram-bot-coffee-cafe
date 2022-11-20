from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove
from keyboards.worker_keyboard import *
from verification.worker_verify import *
from session.worker_session import *
from cash import *
from orders import *
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup


#! =============================================================================================== !#


# Машина состояний для добовления продукта в заказ
class FSMProducts(StatesGroup):
    product = State()
    taste = State()
    additions = State()
    topping = State()


# Машина состояний для выбора способа оплаты
class FSMPaymentMethod(StatesGroup):
    method = State()


#! =============================================================================================== !#


# Команда начала смены
# * @dp.message_handler(commands=['Начать_смену'])
async def start_session(message: types.Message):
    try:
        # Если у мужика смена не начата
        if worker_vefify(message.from_user.id) == True and worker_session_status(message.from_user.id) == False:
            worker_start_session(message.from_user.id)
            append_start_session_on_data(get_worker_name(message.from_user.id))
            await message.answer(f'{get_worker_name(message.from_user.id)}, Вы начали смену!', reply_markup=kb_worker_main_menu)
        # Если у мужика смена уже начата
        elif worker_vefify(message.from_user.id) == True and worker_session_status(message.from_user.id) == True:
            await message.answer(f'{get_worker_name(message.from_user.id)}, Завершите прошлую смену, чтобы начать новую смену!', reply_markup=kb_worker_end_session)
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nОбратитесь к администатору!')
        print(f'worker_handlers Строка №46 - {e}')


#! =============================================================================================== !#


# Команда создания заказа
# * @dp.message_handler(commands=['Создать_заказ'])
async def create_order(message: types.Message):
    try:
        if worker_vefify(message.from_user.id) == True and worker_session_status(message.from_user.id) == True:
            await message.answer(f'Вы начали собирать заказ {create_new_order(message.from_user.id)}', reply_markup=kb_worker_create_order)
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nОбратитесь к администатору!')
        print(f'worker_handlers Строка №60 - {e}')


# Команда добавления продукта
# * @dp.message_handler(commands=['Добавить_продукт'])
async def add_product_to_order(message: types.Message):
    try:
        if worker_vefify(message.from_user.id) == True and worker_session_status(message.from_user.id) == True:
            await FSMProducts.product.set()
            await message.answer('Выберите продукт', reply_markup=kb_worker_append_product)
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nОбратитесь к администатору!')
        print(f'worker_handlers Строка №72 - {e}')


#! =============================================================================================== !#


# Команда выхода из машины состояния (выше всех команд добавления продуктов)
# * @dp.message_handler(Text(equals='отмена!', ignore_case=True), state='*')
async def fsm_products_exit(message: types.Message, state: FSMContext):
    try:
        if worker_vefify(message.from_user.id) == True:
            await state.finish()
            await message.answer('Команда ОТМЕНА!\nВы вернулись в основное меню', reply_markup=kb_worker_main_menu)
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nОбратитесь к администатору!')
        print(f'worker_handlers Строка №87 - {e}')


#! =============================================================================================== !#

# Выбор продукта
# * @dp.message_handler(state=FSMProducts.product)
async def select_product(message: types.Message, state: FSMContext):
    try:
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
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nОбратитесь к администатору!')
        print(f'worker_handlers Строка №119 - {e}')


# Выбор вкуса продукта
# * @dp.message_handler(state=FSMProducts.taste)
async def select_taste(message: types.Message, state: FSMContext):
    try:
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
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nОбратитесь к администатору!')
        print(f'worker_handlers Строка №145 - {e}')


# Выбор посыпки для мороженного
# * @dp.message_handler(state=FSMProducts.additions)
async def select_additions(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['additions'] = ''
        if message.text == 'Завершить':
            if data['additions'] == '':
                async with state.proxy() as data:
                    data['additions'] = f'Без_посыпки '
            await FSMProducts.next()
            await message.answer('Выберите топинг для мороженного', reply_markup=kb_worker_select_topping_icecream)
        elif message.text == 'Без_посыпки':
            async with state.proxy() as data:
                data['additions'] = f'{message.text} '
            await FSMProducts.next()
            await message.answer('Выберите топинг для мороженного', reply_markup=kb_worker_select_topping_icecream)
        else:
            async with state.proxy() as data:
                data['additions'] += f'{message.text} '
            await message.answer(f'Добавлена посыпка: {message.text}')
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nОбратитесь к администатору!')
        print(f'worker_handlers Строка №171 - {e}')


# Выбор топинга для мороженного
# * @dp.message_handler(state=FSMProducts.topping)
async def select_toping(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['toping'] = message.text
        async with state.proxy() as data:
            append_product_to_order(get_dict_items(
                data), get_number_being_created_order(message.from_user.id))
            await message.answer(f'Заказ №{get_number_being_created_order(message.from_user.id)}: {get_all_products(get_number_being_created_order(message.from_user.id))}',  reply_markup=kb_worker_create_order)
        await state.finish()
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nОбратитесь к администатору!')
        print(f'worker_handlers Строка №187 - {e}')


# Команда отмены заказа
# * @dp.message_handler(commands=['Отменить_создание_заказа'])
async def cancel_creating_order(message: types.Message):
    try:
        if worker_vefify(message.from_user.id) == True and worker_session_status(message.from_user.id) == True:
            await message.answer(f'Вы отменили создание заказа №{get_number_being_created_order(message.from_user.id)}. <strong>Заказ удален!</strong>', parse_mode='html', reply_markup=kb_worker_main_menu)
            remove_order(get_number_being_created_order(message.from_user.id))
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nОбратитесь к администатору!')
        print(f'worker_handlers Строка №199 - {e}')


# Команда завершения создания заказа
# * @dp.message_handler(commands=['Завершить_создание_заказа'])
async def complete_creating_order(message: types.Message):
    try:
        if worker_vefify(message.from_user.id) == True and worker_session_status(message.from_user.id) == True:
            await FSMPaymentMethod.method.set()
            await message.answer('Выберите способ оплаты', reply_markup=kb_worker_payment_method)
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nОбратитесь к администатору!')
        print(f'worker_handlers Строка №211 - {e}')


# Команда выбора способа оплаты
# * @dp.message_handler(state=FSMPaymentMethod.method)
async def select_payment_method(message: types.Message, state: FSMContext):
    try:
        async with state.proxy() as data:
            data['method'] = message.text
        if data['method'] == 'КАРТА':
            await message.answer(f'Вы завершили создание заказа №{get_number_being_created_order(message.from_user.id)}: <strong>{get_all_products(get_number_being_created_order(message.from_user.id))}\nОплата по Карте\nЦена: {get_order_price(get_number_being_created_order(message.from_user.id))} Р.</strong> ', parse_mode='html', reply_markup=kb_worker_main_menu)
            load_payment_method(
                True, get_number_being_created_order(message.from_user.id))
            load_order_price(get_order_price(get_number_being_created_order(
                message.from_user.id)), get_number_being_created_order(message.from_user.id))
            complete_create_order(
                get_number_being_created_order(message.from_user.id))
        elif data['method'] == 'НАЛИЧНЫЕ':
            await message.answer(f'Вы завершили создание заказа №{get_number_being_created_order(message.from_user.id)}: <strong>{get_all_products(get_number_being_created_order(message.from_user.id))}\nОплата Наличнми\nЦена: {get_order_price(get_number_being_created_order(message.from_user.id))} Р.</strong> ', parse_mode='html', reply_markup=kb_worker_main_menu)
            load_payment_method(
                False, get_number_being_created_order(message.from_user.id))
            load_order_price(get_order_price(get_number_being_created_order(
                message.from_user.id)), get_number_being_created_order(message.from_user.id))
            complete_create_order(
                get_number_being_created_order(message.from_user.id))
        await state.finish()
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nОбратитесь к администатору!')
        print(f'worker_handlers Строка №239- {e}')


#! =============================================================================================== !#


# Команда просмотра текущих заказов
# * @dp.message_handler(commands=['Текущие_заказы'])
async def check_actuals_orders(message: types.Message):
    try:
        if worker_vefify(message.from_user.id) == True and worker_session_status(message.from_user.id) == True:
            for i in range(get_count_all_orders()):
                # Зачем i+1? чтобы верхняя строка не попадала, иначе выведет None
                if check_running_orders(i+1) == True:
                    await message.answer(f'Текущий Заказ №{i+1}: <strong>{get_all_products(i+1)}\n{get_payment_method_with_text(i+1)}\n Цена: {get_order_price(i+1)} Р.</strong>', parse_mode='html', reply_markup=create_inline_keyboard(i+1))
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nОбратитесь к администатору!')
        print(f'worker_handlers Строка №256 - {e}')


# Команда просмотра завершенных заказов
# * @dp.message_handler(commands=['Выполненные_заказы'])
async def check_complete_orders(message: types.Message):
    try:
        if worker_vefify(message.from_user.id) == True and worker_session_status(message.from_user.id) == True:
            for i in range(get_count_all_orders()):
                # Зачем i+1? чтобы верхняя строка не попадала, иначе выведет None
                if check_completed_orders(i+1) == True:
                    await message.answer(f'Завершенный Заказ №{i+1}: <strong>{get_all_products(i+1)}\n{get_payment_method_with_text(i+1)}\nЦена: {get_order_price(i+1)} Р.</strong>', parse_mode='html')
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nОбратитесь к администатору!')
        print(f'worker_handlers Строка №270 - {e}')


# Тут будут все команды от инлайн кнопок
# * @dp.callback_query_handler()
async def inline_keyboards_commands(callback: types.CallbackQuery):
    try:
        # Команда завершения заказа
        if callback.data.split()[0] == '++':
            await callback.answer(f'🟩 Заказ №{callback.data.split()[1]} Завершен!')
            await callback.message.delete()
            reduce_products_count(callback.data.split()[1])
            change_cash_balance(get_order_price(callback.data.split()[
                                1]), get_payment_method(callback.data.split()[1]), 'увеличить')
            complete_order(callback.data.split()[1])
        # Команда удаления заказа
        elif callback.data.split()[0] == '--':
            await callback.answer(f'🟥 Заказ №{callback.data.split()[1]} Удален!')
            await callback.message.delete()
            remove_order(callback.data.split()[1])
    except Exception as e:
        await callback.answer(f'Что-то пошло не так!\nОбратитесь к администатору!')
        print(f'worker_handlers Строка №292 - {e}')


#! =============================================================================================== !#


# Команда закрытия смены
# * @dp.message_handler(commands=['Закрыть_смену'])
async def end_session(message: types.Message):
    try:
        # Если у мужика смена открыта
        if worker_vefify(message.from_user.id) == True and worker_session_status(message.from_user.id) == True:
            worker_end_session(message.from_user.id)
            append_end_session_on_data(get_worker_name(message.from_user.id))
            await message.answer(f'{get_worker_name(message.from_user.id)}, Закрыл вашу смену', reply_markup=ReplyKeyboardRemove())
        # Если у мужика смена уже закрыта
        elif worker_vefify(message.from_user.id) == True and worker_session_status(message.from_user.id) == False:
            await message.answer(f'<strong>Вы уже закрыли смену!</strong>\nЕсли вы не закрывали смену, обратитесь к Администратору!', reply_markup=ReplyKeyboardRemove(), parse_mode='html')
    except Exception as e:
        await message.answer(f'Что-то пошло не так!\nОбратитесь к администатору!')
        print(f'worker_handlers Строка №312 - {e}')


#! =============================================================================================== !#


# Регистрация всех хендлеров
def register_worker_handlers(dp: Dispatcher):
    try:
        dp.register_message_handler(start_session, commands=['Начать_смену'])
        dp.register_message_handler(create_order, commands=['Создать_заказ'])
        dp.register_message_handler(
            add_product_to_order, commands=['Добавить_продукт'])
        dp.register_message_handler(fsm_products_exit, Text(
            equals='отмена!', ignore_case=True), state='*')
        dp.register_message_handler(select_product, state=FSMProducts.product)
        dp.register_message_handler(select_taste, state=FSMProducts.taste)
        dp.register_message_handler(
            select_additions, state=FSMProducts.additions)
        dp.register_message_handler(select_toping, state=FSMProducts.topping)
        dp.register_message_handler(cancel_creating_order, commands=[
                                    'Отменить_создание_заказа'])
        dp.register_message_handler(complete_creating_order, commands=[
                                    'Завершить_создание_заказа'])
        dp.register_message_handler(
            select_payment_method, state=FSMPaymentMethod.method)
        dp.register_message_handler(
            check_actuals_orders, commands=['Текущие_заказы'])
        dp.register_message_handler(
            check_complete_orders, commands=['Выполненные_заказы'])
        dp.register_callback_query_handler(inline_keyboards_commands)
        dp.register_message_handler(end_session, commands=['Закрыть_смену'])
    except Exception as e:
        print(f'worker_handlers ОШИБКА РЕГИСТРАЦИИ - {e}')
