from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Кнопки старта смены
k_start_session = KeyboardButton('/Начать_смену')

# Кнопки основного меню
k_create_order = KeyboardButton('/Создать_заказ')
k_check_actual_orders = KeyboardButton('/Текущие_заказы')
k_check_completed_orders = KeyboardButton('/Выполненные_заказы')
k_end_session = KeyboardButton('/Закрыть_смену')


# Кнопки для создания заказа


# Инициализируем клавиатуры
# Старта смены
kb_worker_start_session = ReplyKeyboardMarkup(resize_keyboard=True)
# Основного меню
kb_worker_main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
# Если мужик забыл закрыть смену и пытается открыть ее снова
kb_worker_end_session = ReplyKeyboardMarkup(resize_keyboard=True)

# Отображаем клавиатуры
# Старта смены
kb_worker_start_session.row(k_start_session)
# Основного меню
kb_worker_main_menu.add(k_create_order).add(k_check_actual_orders).add(
    k_check_completed_orders).add(k_end_session)
# Если мужик забыл закрыть смену и пытается открыть ее снова
kb_worker_end_session.add(k_end_session)

# kb_client.add(b1).insert(b2)
# kb_worker.row(b1, b2,).row(b1, b2,).row(b1, b2,).row(b1, b2,)
