from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


# Кнопки старта смены
k_start_session = KeyboardButton('/Начать_смену')


# Кнопки основного меню
k_create_order = KeyboardButton('/Создать_заказ')
k_check_actual_orders = KeyboardButton('/Текущие_заказы')
k_check_completed_orders = KeyboardButton('/Выполненные_заказы')
k_end_session = KeyboardButton('/Закрыть_смену')


# Кнопки для сбора заказа
k_order_append_product = KeyboardButton('/Добавить_продукт')
k_complete_create_order = KeyboardButton('/Завершить_создание_заказа')
k_cancel_create_order = KeyboardButton('/Отменить_создание_заказа')


# Кнопки выбора способа оплаты
k_payment_method_card = KeyboardButton('КАРТА')
k_payment_method_paper = KeyboardButton('НАЛИЧНЫЕ')


# Кнопки выбора продукта
k_product_icecream = KeyboardButton('Мороженое')
k_product_tea = KeyboardButton('Чай')
k_product_lemonade = KeyboardButton('Лимонад')
k_product_smoothie = KeyboardButton('Смузи')
k_product_waffle = KeyboardButton('Вафля')
k_product_milkshake = KeyboardButton('Молочный_коктель')
k_cancel_append_product = KeyboardButton('ОТМЕНА')


# Кнопки выбора вкуса мороженого
k_taste_icecream_banana = KeyboardButton('Банан')
k_taste_icecream_orio = KeyboardButton('Орио')
k_taste_icecream_kiwi = KeyboardButton('Киви')
k_taste_icecream_pistachios = KeyboardButton('Фисташки')
k_taste_icecream_nutella = KeyboardButton('Нутелла')
k_taste_icecream_kit_kat = KeyboardButton('Кит_кат')
k_taste_icecream_pineapple = KeyboardButton('Ананас')
k_taste_icecream_rofaello = KeyboardButton('Рофаэлло')
k_taste_icecream_love_is = KeyboardButton('Лове_ис')


# Кнопки выбора посыпок для мороженого
k_addition_icecream_marmalade = KeyboardButton('Мармелад')
k_addition_icecream_cream = KeyboardButton('Сливки')
k_addition_icecream_marshmallows = KeyboardButton('Маршмеллов')
k_addition_icecream_chocolate = KeyboardButton('Шоколад')
k_addition_icecream_coconut = KeyboardButton('Кокос')
k_addition_icecream_mandms = KeyboardButton('m&ms')
k_addition_icecream_none = KeyboardButton('Без_посыпки')
k_addition_icecream_complete = KeyboardButton('Завершить')


# Кнопки добовления топинга для мороженного
k_topping_icecream_strawberry = KeyboardButton('Клубника')
k_topping_icecream_banana = KeyboardButton('Банан')
k_topping_icecream_chocolate = KeyboardButton('Шоколад')
k_topping_icecream_caramel = KeyboardButton('Карамель')
k_topping_icecream_none = KeyboardButton('Без_топинга')


# Кнопки выбора вкуса чая
k_taste_tea_buckthorn_mint = KeyboardButton('Облипиха_мята')
k_taste_tea_raspberry_mint_basil = KeyboardButton('Малина_мята_базилик')
k_taste_tea_strawberry_basil = KeyboardButton('Клубника_базилик')
k_taste_tea_lemon_ginger = KeyboardButton('Лимон_имбирь')


# Кнопки выбора вкуса лимонада
k_taste_lemonade_mojito = KeyboardButton('Мохито')
k_taste_lemonade_lemon = KeyboardButton('Лимон')
k_taste_lemonade_buble_gum = KeyboardButton('Бабл_гам')
k_taste_lemonade_strawberry = KeyboardButton('Клубника')
k_taste_lemonade_coconut = KeyboardButton('Кокос')
k_taste_lemonade_passionflora = KeyboardButton('Маракуйя')


# Кнопки выбора вкуса смузи
k_taste_smoothie_garnet_kiss = KeyboardButton('Гранатовый_поцелуй')
k_taste_smoothie_vit = KeyboardButton('Витаминный')
k_taste_smoothie_grape = KeyboardButton('Виноградник')
k_taste_smoothie_pinacolada = KeyboardButton('Пинаколада')
k_taste_smoothie_tropic = KeyboardButton('Тропикано')


# Кнопки выбора вкуса молочного коктеля
k_taste_milk_banana = KeyboardButton('Банан')
k_taste_milk_chocolate = KeyboardButton('Шоколад')
k_taste_milk_strawberry = KeyboardButton('Клубника')
k_taste_milk_vanilla = KeyboardButton('Ваниль')
k_taste_milk_nutella = KeyboardButton('Нутелла')
k_taste_milk_neskvik = KeyboardButton('Несквик')


# Инлайн кнопки, для завершения заказа или его отмены
def create_inline_keyboard(num_order):
    try:
        k_complete_order = InlineKeyboardButton(
            text=f'🟩 Выполнить заказ №{num_order} 🟩', callback_data=f'++ {num_order}')
        k_remove_order = InlineKeyboardButton(
            text=f'🟥 Удалить заказ №{num_order} 🟥', callback_data=f'-- {num_order}')
        kb_worker_comoleted_and_remove_order = InlineKeyboardMarkup(
            row_width=2)
        return kb_worker_comoleted_and_remove_order.add(
            k_complete_order).add(k_remove_order)
    except Exception as e:
        print(f'worker_keyboard Строка №106 - {e}')


#! Инициализируем клавиатуры
# Старта смены
kb_worker_start_session = ReplyKeyboardMarkup(resize_keyboard=True)
# Основного меню
kb_worker_main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
# Если мужик забыл закрыть смену и пытается открыть ее снова
kb_worker_end_session = ReplyKeyboardMarkup(resize_keyboard=True)
# Сбора заказа
kb_worker_create_order = ReplyKeyboardMarkup(resize_keyboard=True)
# Выбора продукта
kb_worker_append_product = ReplyKeyboardMarkup(resize_keyboard=True)
# Выбора вкуса мороженного
kb_worker_select_taste_icecream = ReplyKeyboardMarkup(resize_keyboard=True)
# Выбора посыпки для мороженного
kb_worker_select_additions_icecream = ReplyKeyboardMarkup(resize_keyboard=True)
# Добовления топинга для мороженного
kb_worker_select_topping_icecream = ReplyKeyboardMarkup(resize_keyboard=True)
# Выбор вкуса чая
kb_worker_select_taste_tea = ReplyKeyboardMarkup(resize_keyboard=True)
# Выбор вкуса лимонада
kb_worker_select_taste_lemonade = ReplyKeyboardMarkup(resize_keyboard=True)
# Выбор вкуса смузи
kb_worker_select_taste_smoothie = ReplyKeyboardMarkup(resize_keyboard=True)
# Выбор вкуса молочного коктеля
kb_worker_select_taste_milkshake = ReplyKeyboardMarkup(resize_keyboard=True)
# Способа оплаты
kb_worker_payment_method = ReplyKeyboardMarkup(resize_keyboard=True)


#! Отображаем клавиатуры
# Старта смены
kb_worker_start_session.row(k_start_session)
# Основного меню
kb_worker_main_menu.add(k_create_order).add(k_check_actual_orders).add(
    k_check_completed_orders).add(k_end_session)
# Если мужик забыл закрыть смену и пытается открыть ее снова
kb_worker_end_session.add(k_end_session)
# Сбора заказа
kb_worker_create_order.row(k_order_append_product).row(
    k_complete_create_order).row(k_cancel_create_order)
# Выбора продукта
kb_worker_append_product.row(k_product_icecream, k_product_tea).row(
    k_product_lemonade, k_product_smoothie).row(k_product_waffle, k_product_milkshake).row(k_cancel_append_product)
# Выбора вкуса мороженного
kb_worker_select_taste_icecream.row(k_taste_icecream_banana, k_taste_icecream_orio).row(k_taste_icecream_kiwi, k_taste_icecream_pistachios).row(
    k_taste_icecream_nutella, k_taste_icecream_kit_kat).row(k_taste_icecream_pineapple, k_taste_icecream_rofaello).row(k_taste_icecream_love_is, ).row(k_cancel_append_product)
# Выбора посыпки для мороженного
kb_worker_select_additions_icecream.row(k_addition_icecream_marmalade, k_addition_icecream_cream).row(k_addition_icecream_marshmallows, k_addition_icecream_chocolate).row(
    k_addition_icecream_coconut, k_addition_icecream_mandms).row(k_addition_icecream_none, k_addition_icecream_complete).row(k_cancel_append_product)
# Добовления топинга для мороженного
kb_worker_select_topping_icecream.row(k_topping_icecream_strawberry, k_topping_icecream_banana).row(
    k_topping_icecream_chocolate, k_topping_icecream_caramel).row(k_topping_icecream_none).row(k_cancel_append_product)
# Выбор вкуса чая
kb_worker_select_taste_tea.row(k_taste_tea_buckthorn_mint, k_taste_tea_raspberry_mint_basil).row(
    k_taste_tea_strawberry_basil, k_taste_tea_lemon_ginger).row(k_cancel_append_product)
# Выбор вкуса лимонада
kb_worker_select_taste_lemonade.row(k_taste_lemonade_mojito, k_taste_lemonade_lemon).row(
    k_taste_lemonade_buble_gum, k_taste_lemonade_strawberry).row(k_taste_lemonade_coconut, k_taste_lemonade_passionflora).row(k_cancel_append_product)
# Выбор вкуса смузи
kb_worker_select_taste_smoothie.row(k_taste_smoothie_garnet_kiss, k_taste_smoothie_vit).row(
    k_taste_smoothie_grape, k_taste_smoothie_pinacolada).row(k_taste_smoothie_tropic).row(k_cancel_append_product)
# Выбор вкуса молочного коктеля
kb_worker_select_taste_milkshake.row(k_taste_milk_banana, k_taste_milk_chocolate).row(
    k_taste_milk_strawberry, k_taste_milk_vanilla).row(k_taste_milk_nutella, k_taste_milk_neskvik).row(k_cancel_append_product)
# Выбора способа оплаты
kb_worker_payment_method.row(k_payment_method_card).row(
    k_payment_method_paper)
