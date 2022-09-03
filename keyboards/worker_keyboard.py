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


# Кнопки выбора вкуса мороженого
k_taste_icecream_banana = KeyboardButton('/Добавить _вкус_банан')
k_taste_icecream_orio = KeyboardButton('/Добавить _вкус_орио')
k_taste_icecream_kiwi = KeyboardButton('/Добавить _вкус_киви')
k_taste_icecream_pistachios = KeyboardButton('/Добавить _вкус_фисташки')
k_taste_icecream_nutella = KeyboardButton('/Добавить _вкус_нутелла')
k_taste_icecream_kit_kat = KeyboardButton('/Добавить _вкус_кит-кат')
k_taste_icecream_pineapple = KeyboardButton('/Добавить _вкус_ананас')
k_taste_icecream_rofaello = KeyboardButton('/Добавить _вкус_рофаэлло')
k_taste_icecream_love_is = KeyboardButton('/Добавить _вкус_лове-ис')


# Кнопки выбора посыпок для мороженого
k_addition_icecream_marmalade = KeyboardButton('/Добавить _посыпку_мармелад')
k_addition_icecream_cream = KeyboardButton('/Добавить _посыпку_сливки')
k_addition_icecream_marshmallows = KeyboardButton(
    '/Добавить _посыпку_маршмеллов')
k_addition_icecream_chocolate = KeyboardButton('/Добавить _посыпку_шоколад')
k_addition_icecream_coconut = KeyboardButton('/Добавить _посыпку_кокос')
k_addition_icecream_mandms = KeyboardButton('/Добавить _посыпку_m&ms')
k_addition_icecream_none = KeyboardButton('/Добавить _без_посыпки')
k_complete_append_addition_icecream = KeyboardButton(
    '/Завершить_добовление_посыпок')


# Кнопки добовления топинга
k_topping_icecream_strawberry = KeyboardButton('/Добавить _топинг_клубника')
k_topping_icecream_banana = KeyboardButton('/Добавить _топинг_банан')
k_topping_icecream_chocolate = KeyboardButton('/Добавить _топинг_шоколад')
k_topping_icecream_caramel = KeyboardButton('/Добавить _топинг_карамель')
k_topping_icecream_none = KeyboardButton('/Добавить _без_топинга')


# ! Тут будут некст кнопки
# Кнопки вкуса лимонада
# Кнопки вкуса смузи
# Кнопки вкуса чая
# Кнопки вкус молочного коктеля
# Кнопки


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
# Выбора вкуса мороженного
kb_worker_select_taste_icecream = ReplyKeyboardMarkup(resize_keyboard=True)
# Выбора посыпки для мороженного
kb_worker_select_additions_icecream = ReplyKeyboardMarkup(resize_keyboard=True)
# Добовления топинга
kb_worker_select_topping_icecream = ReplyKeyboardMarkup(resize_keyboard=True)


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
# Выбора вкуса мороженного
kb_worker_select_taste_icecream.row(k_taste_icecream_banana, k_taste_icecream_orio).row(k_taste_icecream_kiwi, k_taste_icecream_pistachios).row(
    k_taste_icecream_nutella, k_taste_icecream_kit_kat).row(k_taste_icecream_pineapple, k_taste_icecream_rofaello).row(k_taste_icecream_love_is, )
# Выбора посыпки для мороженного
kb_worker_select_additions_icecream.row(k_addition_icecream_marmalade, k_addition_icecream_cream).row(k_addition_icecream_marshmallows, k_addition_icecream_chocolate).row(
    k_addition_icecream_coconut, k_addition_icecream_mandms).row(k_addition_icecream_none)
# Добовления топинга
kb_worker_select_topping_icecream.row(k_topping_icecream_strawberry, k_topping_icecream_banana).row(
    k_topping_icecream_chocolate, k_topping_icecream_caramel).row(k_topping_icecream_none)
