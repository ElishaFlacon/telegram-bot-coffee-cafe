from aiogram import types, Dispatcher
from keyboards import *
from verification import *
from create import dp


# Команда старта
# * @dp.message_handler(commands=['start', 'старт'])
async def start_working(message: types.Message):
    if admin_vefify(message.from_user.id) == True:
        await message.answer(f'Здравствуйте, Администратор, {message.from_user.full_name}!', reply_markup=None)
    elif worker_vefify(message.from_user.id) == True:
        await message.answer(f'Здравствуйте, {message.from_user.full_name}, вы хотиет начать смену?', reply_markup=kb_worker_start_session)
    else:
        await message.answer(f'Здравствуйте, вы не зарегистрированный пользователь, обратитесь к Администратору и предоставте ваш ID: <strong>{message.from_user.id}</strong>', parse_mode='html')


#! Регистрация всех хендлеров
def register_other_handlers(dp: Dispatcher):
    dp.register_message_handler(start_working, commands=['start', 'старт'])
