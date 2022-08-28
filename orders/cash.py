import openpyxl
import datetime


DATA = openpyxl.load_workbook('data/data.xlsx')
WORKERS_SHEET = DATA['workers']
ORDERS_SHEET = DATA['orders']


# Добовляем цену продукта в заказ
def append_product_price_to_order():
    pass
