from data import *


# Получаем продукт
def get_product(product):
    product_name = str(product).split()
    for i in product_name:
        if i.find('_вкус_') == 0:
            pass
        elif i.find('_посыпку_') == 0:
            pass
        elif i.find('_') == 0:
            return i[1:]


# Получаем все продукты из заказа
def get_all_products(num_order):
    products = ''
    max_rw_orders = ORDERS_SHEET.max_row
    for i in range(max_rw_orders):
        if str(ORDERS_SHEET[f'B{i+1}'].value) == str(num_order):
            for i in str(ORDERS_SHEET[f'G{i+1}'].value).split():
                if i.find('-') == 0:
                    if i == '-мороженое':
                        products += i[1:] + ' '
                    else:
                        products += i[1:] + ', '
                elif i.find(':') == 0:
                    products += 'вкус: ' + i[1:] + ' '
                elif i.find('+') == 0:
                    products += i + ', '
    return str(products)


# Добовляем продукты в заказ
def append_product_to_order(product, num_order):
    max_rw_orders = ORDERS_SHEET.max_row
    for i in range(max_rw_orders):
        if str(ORDERS_SHEET[f'B{i+1}'].value) == str(num_order) and str(ORDERS_SHEET[f'C{i+1}'].value) == str('Создается'):
            if ORDERS_SHEET[f'G{i+1}'].value != None:
                ORDERS_SHEET[f'G{i+1}'] = f'{ORDERS_SHEET[f"G{i+1}"].value} -{product}'
            elif ORDERS_SHEET[f'G{i+1}'].value == None:
                ORDERS_SHEET[f'G{i+1}'] = f'-{product}'
    save_data()


# Добовляем дополнительные продукты в заказ, типо вкус мороженого
def append_additional_product_to_order(product, num_order):
    max_rw_orders = ORDERS_SHEET.max_row
    for i in range(max_rw_orders):
        if str(ORDERS_SHEET[f'B{i+1}'].value) == str(num_order) and str(ORDERS_SHEET[f'C{i+1}'].value) == str('Создается'):
            if ORDERS_SHEET[f'G{i+1}'].value != None:
                ORDERS_SHEET[f'G{i+1}'] = f'{ORDERS_SHEET[f"G{i+1}"].value} +{product}'
    save_data()
