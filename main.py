from aiogram import executor
from create import dp
from handlers import *

# ТЕСТ
#! Инициализируем хендлеры
try:
    register_admin_handlers(dp)
    register_worker_handlers(dp)
    register_other_handlers(dp)
except Exception as e:
    print(f'main ОШИБКА ИНИЦИАЛИЗАЦИИ ХЕНДЛЕРОВ - {e}')


#! Запуск
try:
    if __name__ == '__main__':
        executor.start_polling(dp, skip_updates=True,
                               on_startup=print('!ПУСК!'))
except Exception as e:
    print(f'main ОШИБКА ЗАПУСКА ПРИЛОЖЕНИЯ - {e}')
