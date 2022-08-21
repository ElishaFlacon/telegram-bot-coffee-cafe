import openpyxl
import datetime


DATA = openpyxl.load_workbook('data/data.xlsx')
WORKERS_SHEET = DATA['workers']
ORDERS_SHEET = DATA['orders']


def worker_get_product(product):
    product_name = str(product).split()
    for i in product_name:
        if i.find('_') == 0:
            return i[1:]


def worker_create_new_order(worker_id):
    max_rw_workers = WORKERS_SHEET.max_row
    max_rw_orders = ORDERS_SHEET.max_row
    for i in range(max_rw_workers):
        if str(WORKERS_SHEET[f'C{i+1}'].value) == str(worker_id):
            for i in range(max_rw_orders + 1):
                if ORDERS_SHEET[f'A{i+1}'].value == None:
                    ORDERS_SHEET[f'A{i+1}'] = str(worker_id)
                    ORDERS_SHEET[f'B{i+1}'] = str(int(
                        ORDERS_SHEET[f'A{i+1}'].row - 1))
                    ORDERS_SHEET[f'C{i+1}'] = str('Создается')
                    ORDERS_SHEET[f'F{i+1}'] = str(datetime.datetime.now())
                    DATA.save('data/data.xlsx')
                    DATA.close()
                    return str(int(ORDERS_SHEET[f'A{i+1}'].row - 1))


def worker_get_count_order(worker_id):
    num_order = []
    max_rw_orders = ORDERS_SHEET.max_row
    for i in range(max_rw_orders):
        if str(ORDERS_SHEET[f'A{i+1}'].value) == str(worker_id) and str(ORDERS_SHEET[f'C{i+1}'].value) == str('Создается'):
            num_order.append(int(ORDERS_SHEET[f'B{i+1}'].value))
    return str(max(num_order))


def worker_append_product_to_order(product):
    max_rw = ORDERS_SHEET.max_row
    for i in range(max_rw):
        if str(ORDERS_SHEET[f'C{i+1}'].value) == str(''):
            ORDERS_SHEET[f'D{i+1}'] = 'Да'
    DATA.save('data/data.xlsx')
    DATA.close()


def worker_complete_create_order():
    pass


def worker_complete_order():
    pass


def worker_remove_order():
    pass


def worker_check_completed_orders():
    pass


def worker_check_actual_orders():
    pass
