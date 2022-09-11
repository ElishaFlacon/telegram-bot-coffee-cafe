from data import *


# Получаем продукт из словоря
def get_dict_items(dt):
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


# Получаем все продукты из заказа
def get_all_products(num_order):
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


# Добовляем продукты в заказ
def append_product_to_order(product, num_order):
    max_rw_orders = ORDERS_SHEET.max_row
    for i in range(max_rw_orders):
        if str(ORDERS_SHEET[f'B{i+1}'].value) == str(num_order) and str(ORDERS_SHEET[f'C{i+1}'].value) == str('Создается'):
            if ORDERS_SHEET[f'G{i+1}'].value == None:
                ORDERS_SHEET[f'G{i+1}'] = product
            else:
                ORDERS_SHEET[f'G{i+1}'] = ORDERS_SHEET[f'G{i+1}'].value + product
    save_data()
