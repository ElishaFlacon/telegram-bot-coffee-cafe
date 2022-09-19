from data import *


def admin_vefify(admin_id):
    try:
        max_rw = ADMINS_SHEET.max_row
        for i in range(max_rw):
            if str(ADMINS_SHEET[f'C{i+1}'].value) == str(admin_id):
                return True
    except Exception as e:
        print(f'admin_verify Строка №11 - {e}')
