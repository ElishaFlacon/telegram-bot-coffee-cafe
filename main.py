from aiogram import executor
from create import dp
from handlers import *


#! Инициализируем хендлеры
register_worker_handlers(dp)
register_other_handlers(dp)
register_admin_handlers(dp)


#! Запуск
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=print('!ПУСК!'))
