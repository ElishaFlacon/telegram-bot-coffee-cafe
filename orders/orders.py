from data import *
import datetime
from orders.products import get_all_products


# Создаем новый заказ
def create_new_order(worker_id):
    max_rw_workers = WORKERS_SHEET.max_row
    max_rw_orders = ORDERS_SHEET.max_row
    for i in range(max_rw_workers):
        if str(WORKERS_SHEET[f'C{i+1}'].value) == str(worker_id):
            # +1 чтобы захватывалась пустая ячейка
            for i in range(max_rw_orders + 1):
                if ORDERS_SHEET[f'A{i+1}'].value == None:
                    ORDERS_SHEET[f'A{i+1}'] = str(worker_id)
                    ORDERS_SHEET[f'B{i+1}'] = str(int(
                        ORDERS_SHEET[f'A{i+1}'].row - 1))
                    ORDERS_SHEET[f'C{i+1}'] = 'Создается'
                    ORDERS_SHEET[f'F{i+1}'] = str(datetime.datetime.now())
                    save_data()
                    return str(int(ORDERS_SHEET[f'A{i+1}'].row - 1))


# Завершаем создание заказа
def complete_create_order(num_order):
    max_rw_orders = ORDERS_SHEET.max_row
    for i in range(max_rw_orders):
        if str(ORDERS_SHEET[f'B{i+1}'].value) == str(num_order) and str(ORDERS_SHEET[f'C{i+1}'].value) == 'Создается':
            ORDERS_SHEET[f'C{i+1}'] = 'Выполняется'
            ORDERS_SHEET[f'F{i+1}'] = str(datetime.datetime.now())
    save_data()


# Получаем количество всех заказов
def get_count_all_orders():
    # Минусуем чтобы последняя строка не попадала
    # Иначе будет на выходе None в функции check_actua_orders
    return int(ORDERS_SHEET.max_row) - 1


# Получаем номер заказа (последний создающийся заказ)
def get_number_being_created_order(worker_id):
    num_order = []
    max_rw_orders = ORDERS_SHEET.max_row
    for i in range(max_rw_orders):
        if str(ORDERS_SHEET[f'A{i+1}'].value) == str(worker_id) and str(ORDERS_SHEET[f'C{i+1}'].value) == 'Создается':
            num_order.append(str(int(ORDERS_SHEET[f'B{i+1}'].value)))
    return str(max(num_order))


# Получаем номер заказа (последний выполняющийся заказ)
def get_number_process_order(worker_id):
    num_order = []
    max_rw_orders = ORDERS_SHEET.max_row
    for i in range(max_rw_orders):
        if str(ORDERS_SHEET[f'A{i+1}'].value) == str(worker_id) and str(ORDERS_SHEET[f'C{i+1}'].value) == 'Выполняется':
            num_order.append(str(int(ORDERS_SHEET[f'B{i+1}'].value)))
    return str(max(num_order))


# Выполняем заказ
def complete_order(num_order):
    max_rw_orders = ORDERS_SHEET.max_row
    for i in range(max_rw_orders):
        if str(ORDERS_SHEET[f'B{i+1}'].value) == str(num_order) and str(ORDERS_SHEET[f'C{i+1}'].value) == 'Выполняется':
            ORDERS_SHEET[f'C{i+1}'] = 'Завершен'
    save_data()


# Отменяем заказ
def remove_order(num_order):
    max_rw_orders = ORDERS_SHEET.max_row
    for i in range(max_rw_orders):
        if str(ORDERS_SHEET[f'B{i+1}'].value) == str(num_order) and str(ORDERS_SHEET[f'C{i+1}'].value) != 'Завершен' and str(ORDERS_SHEET[f'C{i+1}'].value) != 'Удален':
            # Почему именно удален???
            # Иначе появлялись бы пустые места между заказами, при их удалении
            # Вообще получалась бы жопа
            # Завершенные заказы удалить будет нельзя
            # Это для безопасности
            # Ну а также можно будет посмотреть все удаленные заказы ... в экселе))
            ORDERS_SHEET[f'C{i+1}'] = 'Удален'
    save_data()


# Смотрим выполняющиеся заказы
def check_running_orders(num_order):
    max_rw_orders = ORDERS_SHEET.max_row
    for i in range(max_rw_orders):
        if str(ORDERS_SHEET[f'B{i+1}'].value) == str(num_order) and str(ORDERS_SHEET[f'C{i+1}'].value) == 'Выполняется':
            return True


# Смотрим выполненные заказы
def check_completed_orders(num_order):
    max_rw_orders = ORDERS_SHEET.max_row
    for i in range(max_rw_orders):
        if str(ORDERS_SHEET[f'B{i+1}'].value) == str(num_order) and str(ORDERS_SHEET[f'C{i+1}'].value) == 'Завершен':
            return True
