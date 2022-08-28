from data import *


def worker_vefify(worker_id):
    max_rw = WORKERS_SHEET.max_row
    for i in range(max_rw):
        if str(WORKERS_SHEET[f'C{i+1}'].value) == str(worker_id):
            return True
