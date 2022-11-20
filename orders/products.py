from data import *


# Получаем продукт из словоря
def get_dict_items(dt):
    try:
        return_str = ''
        for key in dt:
            if key == 'product':
                return_str += f'-{dt[key]} '
            elif key == 'taste':
                return_str += f':{dt[key]} '
            elif key == 'additions':
                for i in dt[key].split():
                    return_str += f'+{i} '
            elif key == 'toping':
                return_str += f'={dt[key]} '
        return f'{return_str[:-1]}; '
    except Exception as e:
        print(f'products Строка №20 - {e}')


# Получаем все продукты из заказа
def get_all_products(num_order):
    try:
        products = ''
        max_rw_orders = ORDERS_SHEET.max_row
        for i in range(max_rw_orders):
            if str(ORDERS_SHEET[f'B{i+1}'].value) == str(num_order):
                for i in str(ORDERS_SHEET[f'G{i+1}'].value).split():
                    if i.find('-') == 0:
                        products += f'{i[1:]} '
                    elif i.find(':') == 0:
                        products += f'вкус: {i[1:]} '
                    elif i.find('+') == 0:
                        products += f'П.{i[1:]} '
                    elif i.find('=') == 0:
                        products += f'Т.{i[1:]} '
        return f'{products[:-1]}'
    except Exception as e:
        print(f'products Строка №41 - {e}')


# Добовляем продукты в заказ
def append_product_to_order(product, num_order):
    try:
        max_rw_orders = ORDERS_SHEET.max_row
        for i in range(max_rw_orders):
            if str(ORDERS_SHEET[f'B{i+1}'].value) == str(num_order) and str(ORDERS_SHEET[f'C{i+1}'].value) == str('Создается'):
                if ORDERS_SHEET[f'G{i+1}'].value == None:
                    ORDERS_SHEET[f'G{i+1}'] = product
                else:
                    ORDERS_SHEET[f'G{i+1}'] = ORDERS_SHEET[f'G{i+1}'].value + product
        save_data()
    except Exception as e:
        print(f'products Строка №56 - {e}')


# Уменьшаем количество продуктов
def reduce_products_count(num_order):
    try:
        max_rw_products = PRODUCTS_SHEET.max_row
        max_rw_orders = ORDERS_SHEET.max_row
        for i in range(max_rw_orders):
            if str(ORDERS_SHEET[f'B{i+1}'].value) == str(num_order):
                # Пробел в сплите, после ; нужен, просто необходим, наверно))
                # [:-1] нужен, зачем? а потому что в конце массива появлялась пустая строка
                # через иф не убиралась, так что вырежем так))
                for j in ORDERS_SHEET[f'G{i+1}'].value.split('; ')[:-1]:
                    for l in range(max_rw_products):
                        # Тут проверка на продукт и вкус
                        if j.lower().find(str(PRODUCTS_SHEET[f'A{l+1}'].value)) == 0:
                            PRODUCTS_SHEET[f'C{l+1}'] = str(
                                int(PRODUCTS_SHEET[f'C{l+1}'].value) - 1)
        save_data()
    except Exception as e:
        print(f'products Строка №77 - {e}')


# Увеличиваем количество продуктов
def increasing_products_count(num_order, count):
    try:
        max_rw_products = PRODUCTS_SHEET.max_row
        max_rw_orders = ORDERS_SHEET.max_row
        for i in range(max_rw_orders):
            if str(ORDERS_SHEET[f'B{i+1}'].value) == str(num_order):
                # Пробел в сплите, после ; нужен, просто необходим, наверно))
                # [:-1] нужен, зачем? а потому что в конце массива появлялась пустая строка
                # через иф не убиралась, так что вырежем так :))
                for j in ORDERS_SHEET[f'G{i+1}'].value.split('; ')[:-1]:
                    for l in range(max_rw_products):
                        # Тут проверка на продукт и вкус
                        if j.lower().find(str(PRODUCTS_SHEET[f'A{l+1}'].value)) == 0:
                            PRODUCTS_SHEET[f'C{l+1}'] = str(
                                int(PRODUCTS_SHEET[f'C{l+1}'].value) + int(count))
        save_data()
    except Exception as e:
        print(f'products Строка №98 - {e}')
