from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


# Кнопки основного меню
k_admin_workers = KeyboardButton('/Сотрудники')
k_admin_products = KeyboardButton('/Продукты')
k_admin_cash = KeyboardButton('/Касса')


# Дополнительные необходимые кнопки
k_admin_back = KeyboardButton('НАЗАД')
k_admin_cancel = KeyboardButton('ОТМЕНА')


# Кнопки меню сотрудников
k_admin_check_sessions_status = KeyboardButton('/Активные_смены')
k_admin_check_worker_sessions = KeyboardButton('/Смены_сотрудников')
k_admin_change_worker = KeyboardButton('/Изменить_список_сотрудников')


# Кнопки меню смены сотрудников
k_admin_today_date = KeyboardButton('Сегодня')


# Кнопки меню изменить список сотрудников
k_admin_append_worker = KeyboardButton('Добавить')
k_admin_remove_worker = KeyboardButton('Удалить')


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
# Инициализация клавиатуры меню смен сотрудников
kb_admin_worker_sessions_menu = ReplyKeyboardMarkup(resize_keyboard=True)
# Инициализация клавиатуры меню изменения сотрудников
kb_admin_worker_change_menu = ReplyKeyboardMarkup(resize_keyboard=True)
# Инициализация клавиатуры меню продуктов
kb_admin_products_menu = ReplyKeyboardMarkup(resize_keyboard=True)
# Инициализация клавиатуры меню кассы
kb_admin_cash_menu = ReplyKeyboardMarkup(resize_keyboard=True)
# Отображение клавиатуры ОТМЕНА!
kb_admin_cancel = ReplyKeyboardMarkup(resize_keyboard=True)


# Отображение клавиатуры основного меню
kb_admin_main_menu.row(k_admin_workers).row(k_admin_products).row(k_admin_cash)
# Отображение клавиатуры меню сотрудников
kb_admin_workers_menu.row(
    k_admin_check_sessions_status).row(k_admin_check_worker_sessions).row(k_admin_change_worker).row(k_admin_back)
# Отображение клавиатуры меню смен сотрудников
kb_admin_worker_sessions_menu.row(k_admin_today_date).row(k_admin_cancel)
# Отображение клавиатуры меню изменения сотрудников
kb_admin_worker_change_menu.row(
    k_admin_append_worker).row(k_admin_remove_worker).row(k_admin_cancel)
# Отображение клавиатуры меню продуктов
kb_admin_products_menu.row(k_admin_append_products).row(
    k_admin_append_dishes).row(k_admin_back)
# Отображение клавиатуры меню кассы
kb_admin_cash_menu.row(k_admin_check_cash).row(
    k_admin_increment_cash).row(k_admin_decrement_cash).row(k_admin_back)
# Отображение клавиатуры ОТМЕНА!
kb_admin_cancel.row(k_admin_cancel)
