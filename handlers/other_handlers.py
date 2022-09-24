from aiogram import types, Dispatcher
from keyboards import *
from verification import *
from create import dp


# Команда старта
# * @dp.message_handler(commands=['start', 'старт'])
async def start_working(message: types.Message):
    try:
        if admin_verify(message.from_user.id) == True:
            await message.answer(f'Здравствуйте, Администратор, {message.from_user.full_name}!', reply_markup=kb_admin_main_menu)
        elif worker_vefify(message.from_user.id) == True:
            await message.answer(f'Здравствуйте, {get_worker_name(message.from_user.id)}, вы хотите начать смену?', reply_markup=kb_worker_start_session)
        else:
            await message.answer(f'Здравствуйте, вы не зарегистрированный пользователь, обратитесь к Администратору и предоставте ваш ID: <strong>{message.from_user.id}</strong>', parse_mode='html')
    except Exception as e:
        print(f'other_handlers Строка №18 - {e}')


#! Регистрация всех хендлеров
def register_other_handlers(dp: Dispatcher):
    try:
        dp.register_message_handler(start_working, commands=['start', 'старт'])
    except Exception as e:
        print(f'other_handlers ОШИБКА РЕГИСТРАЦИИ ХЕНДЛЕРОВ - {e}')
