from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


# Кнопки основного меню
k_admin_workers = KeyboardButton('/Сотрудники')
k_admin_products = KeyboardButton('/Продукты')
k_admin_cash = KeyboardButton('/Касса')


# Дополнительные необходимые кнопки
k_admin_back = KeyboardButton('НАЗАД')
k_admin_cancel = KeyboardButton('Отмена')


# Кнопки меню сотрудников
k_admin_check_worker_sessions = KeyboardButton('/Смены_сотрудников')
k_admin_check_sessions_status = KeyboardButton('/Кто_на_смене')
k_admin_append_new_worker = KeyboardButton('/Добавить_сотрудника')
k_admin_delete_worker = KeyboardButton('/Удалить_сотрудника')


# Кнопки меню продуктов
k_admin_append_products = KeyboardButton('/Добавить_продукты')
k_admin_append_dishes = KeyboardButton('/Добавить_посуду')


# Кнопки меню кассы
k_admin_check_cash = KeyboardButton('/Баланс')
k_admin_increment_cash = KeyboardButton('/Увеличить_баланс')
k_admin_decrement_cash = KeyboardButton('/Уменьшить_баланс')


# Инициализация клавиатуры основного меню
kb_admin_main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
# Инициализация клавиатуры меню сотрудников
kb_admin_workers_menu = ReplyKeyboardMarkup(resize_keyboard=True)
# Инициализация клавиатуры меню продуктов
kb_admin_products_menu = ReplyKeyboardMarkup(resize_keyboard=True)
# Инициализация клавиатуры меню кассы
kb_admin_cash_menu = ReplyKeyboardMarkup(resize_keyboard=True)


# Отображение клавиатуры основного меню
kb_admin_main_menu.row(k_admin_workers).row(k_admin_products).row(k_admin_cash)
# Отображение клавиатуры меню сотрудников
kb_admin_workers_menu.row(k_admin_check_worker_sessions).row(
    k_admin_check_sessions_status).row(k_admin_append_new_worker).row(k_admin_delete_worker)
# Отображение клавиатуры меню продуктов
kb_admin_products_menu.row(k_admin_append_products).row(k_admin_append_dishes)
# Отображение клавиатуры меню кассы
kb_admin_cash_menu.row(k_admin_check_cash).row(
    k_admin_increment_cash).row(k_admin_decrement_cash)
