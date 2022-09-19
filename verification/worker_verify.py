from data import *


def worker_vefify(worker_id):
    try:
        max_rw = WORKERS_SHEET.max_row
        for i in range(max_rw):
            if str(WORKERS_SHEET[f'C{i+1}'].value) == str(worker_id):
                return True
    except Exception as e:
        print(f'worker_verify Строка №11 - {e}')


def get_worker_name(worker_id):
    try:
        max_rw = WORKERS_SHEET.max_row
        for i in range(max_rw):
            if str(WORKERS_SHEET[f'C{i+1}'].value) == str(worker_id):
                return str(WORKERS_SHEET[f'B{i+1}'].value)
    except Exception as e:
        print(f'worker_verify Строка №21 - {e}')
