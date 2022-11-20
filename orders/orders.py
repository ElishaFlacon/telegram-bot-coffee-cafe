from data import *
import datetime


# Создаем новый заказ
def create_new_order(worker_id):
    try:
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
                        ORDERS_SHEET[f'F{i+1}'] = str(
                            datetime.datetime.now())[:-7]
                        save_data()
                        return str(int(ORDERS_SHEET[f'A{i+1}'].row - 1))
    except Exception as e:
        print(f'orders Строка №24 - {e}')


# Завершаем создание заказа
def complete_create_order(num_order):
    try:
        max_rw_orders = ORDERS_SHEET.max_row
        for i in range(max_rw_orders):
            if str(ORDERS_SHEET[f'B{i+1}'].value) == str(num_order) and str(ORDERS_SHEET[f'C{i+1}'].value) == 'Создается':
                ORDERS_SHEET[f'C{i+1}'] = 'Выполняется'
                ORDERS_SHEET[f'F{i+1}'] = str(datetime.datetime.now())[:-7]
        save_data()
    except Exception as e:
        print(f'orders Строка №37 - {e}')


# Получаем количество всех заказов
def get_count_all_orders():
    try:
        # Минусуем чтобы последняя строка не попадала
        # Иначе будет на выходе None в функции check_actua_orders
        return int(ORDERS_SHEET.max_row) - 1
    except Exception as e:
        print(f'orders Строка №47 - {e}')


# Получаем номер заказа (последний создающийся заказ)
def get_number_being_created_order(worker_id):
    try:
        num_order = []
        max_rw_orders = ORDERS_SHEET.max_row
        for i in range(max_rw_orders):
            if str(ORDERS_SHEET[f'A{i+1}'].value) == str(worker_id) and str(ORDERS_SHEET[f'C{i+1}'].value) == 'Создается':
                num_order.append(str(int(ORDERS_SHEET[f'B{i+1}'].value)))
        return str(max(num_order))
    except Exception as e:
        print(f'orders Строка №60 - {e}')


# Получаем номер заказа (последний выполняющийся заказ)
def get_number_process_order(worker_id):
    try:
        num_order = []
        max_rw_orders = ORDERS_SHEET.max_row
        for i in range(max_rw_orders):
            if str(ORDERS_SHEET[f'A{i+1}'].value) == str(worker_id) and str(ORDERS_SHEET[f'C{i+1}'].value) == 'Выполняется':
                num_order.append(str(int(ORDERS_SHEET[f'B{i+1}'].value)))
        return str(max(num_order))
    except Exception as e:
        print(f'orders Строка №73 - {e}')


# Выполняем заказ
def complete_order(num_order):
    try:
        max_rw_orders = ORDERS_SHEET.max_row
        for i in range(max_rw_orders):
            if str(ORDERS_SHEET[f'B{i+1}'].value) == str(num_order) and str(ORDERS_SHEET[f'C{i+1}'].value) == 'Выполняется':
                ORDERS_SHEET[f'C{i+1}'] = 'Завершен'
        save_data()
    except Exception as e:
        print(f'orders Строка №85 - {e}')


# Отменяем заказ
def remove_order(num_order):
    try:
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
    except Exception as e:
        print(f'orders Строка №103 - {e}')


# Смотрим выполняющиеся заказы
def check_running_orders(num_order):
    try:
        max_rw_orders = ORDERS_SHEET.max_row
        for i in range(max_rw_orders):
            if str(ORDERS_SHEET[f'B{i+1}'].value) == str(num_order) and str(ORDERS_SHEET[f'C{i+1}'].value) == 'Выполняется':
                return True
    except Exception as e:
        print(f'orders Строка №114 - {e}')


# Смотрим выполненные заказы
def check_completed_orders(num_order):
    try:
        max_rw_orders = ORDERS_SHEET.max_row
        for i in range(max_rw_orders):
            if str(ORDERS_SHEET[f'B{i+1}'].value) == str(num_order) and str(ORDERS_SHEET[f'C{i+1}'].value) == 'Завершен':
                return True
    except Exception as e:
        print(f'orders Строка №125 - {e}')
