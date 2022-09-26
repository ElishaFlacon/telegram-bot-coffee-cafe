from data import *


def admin_verify(admin_id):
    try:
        max_rw = ADMINS_SHEET.max_row
        for i in range(max_rw):
            if str(ADMINS_SHEET[f'C{i+1}'].value) == str(admin_id):
                return True
    except Exception as e:
        print(f'admin_verify Строка №11 - {e}')


# Добавление новоо сотрудника, почему эта функция здесь, спросите
# А воооот, потому что могу
# А вообще стоило разбить почти пол проекта на еще более меньшие компоненты
# Учту это на будующее
# Но а сейчас я 'устану' это делать
# Я не думал что бот выйдет на 1000+ строк
# Так, прикинул, ну там на 400 - 600...
def create_new_worker():
    pass
