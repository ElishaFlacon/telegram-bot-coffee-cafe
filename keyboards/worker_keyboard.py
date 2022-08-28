from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


# Кнопки старта смены
k_start_session = KeyboardButton('/Начать_смену')


# Кнопки основного меню
k_create_order = KeyboardButton('/Создать_заказ')
k_check_actual_orders = KeyboardButton('/Текущие_заказы')
k_check_completed_orders = KeyboardButton('/Выполненные_заказы')
k_end_session = KeyboardButton('/Закрыть_смену')


# Кнопки для сбора заказа
k_order_icecream = KeyboardButton('/Добавить _мороженое')
k_order_tea = KeyboardButton('/Добавить _чай')
k_order_lemonade = KeyboardButton('/Добавить _лимонад')
k_order_smoothie = KeyboardButton('/Добавить _смузи')
k_order_waffle = KeyboardButton('/Добавить _вафлю')
k_order_milkshake = KeyboardButton('/Добавить _молочный_коктель')
k_complete_create_order = KeyboardButton('/Завершить_создание_заказа')
k_cancel_create_order = KeyboardButton('/Отменить_создание_заказа')


# Инлайн кнопки, для завершения заказа или его отмены
def create_inline_keyboard(num_order):
    k_complete_order = InlineKeyboardButton(
        text=f'🟩 Выполнить заказ №{num_order} 🟩', callback_data=f'++ {num_order}')
    k_remove_order = InlineKeyboardButton(
        text=f'🟥 Удалить заказ №{num_order} 🟥', callback_data=f'-- {num_order}')
    kb_worker_comoleted_and_remove_order = InlineKeyboardMarkup(row_width=2)
    return kb_worker_comoleted_and_remove_order.add(
        k_complete_order).add(k_remove_order)


# Инициализируем клавиатуры
# Старта смены
kb_worker_start_session = ReplyKeyboardMarkup(resize_keyboard=True)
# Основного меню
kb_worker_main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
# Если мужик забыл закрыть смену и пытается открыть ее снова
kb_worker_end_session = ReplyKeyboardMarkup(resize_keyboard=True)
# Сбора заказа
kb_worker_create_order = ReplyKeyboardMarkup(resize_keyboard=True)
# Инлайн клавиатура, для завершения заказа или его отмены


# Отображаем клавиатуры
# Старта смены
kb_worker_start_session.row(k_start_session)
# Основного меню
kb_worker_main_menu.add(k_create_order).add(k_check_actual_orders).add(
    k_check_completed_orders).add(k_end_session)
# Если мужик забыл закрыть смену и пытается открыть ее снова
kb_worker_end_session.add(k_end_session)
# Сбора заказа
kb_worker_create_order.row(k_order_icecream, k_order_tea).row(
    k_order_lemonade, k_order_smoothie).row(k_order_waffle, k_order_milkshake).row(k_complete_create_order).row(k_cancel_create_order)
