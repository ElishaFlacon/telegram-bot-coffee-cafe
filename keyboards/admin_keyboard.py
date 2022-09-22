from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


# Кнопки основного меню
k_admin_check_worker_sessions = KeyboardButton(
    '/Просмотреть_смены_сотрудников')
k_admin_append_new_worker = KeyboardButton('/Добавить_сотрудника')
k_admin_delete_worker = KeyboardButton('/Удалить_сотрудника')
k_admin_append_products = KeyboardButton('/Добавить_продукты')
k_admin_check_cash = KeyboardButton('/Касса')


# Инициализация клавиатуры основного меню
kb_admin_main_menu = ReplyKeyboardMarkup(resize_keyboard=True)


# Отображение клавиатуры основного меню
kb_admin_main_menu.row(k_admin_check_worker_sessions).row(k_admin_append_new_worker).row(
    k_admin_delete_worker).row(k_admin_append_products).row(k_admin_check_cash)
