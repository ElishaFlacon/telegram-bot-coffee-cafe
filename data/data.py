import openpyxl


try:
    DATA = openpyxl.load_workbook('data/data.xlsx')
    WORKERS_SHEET = DATA['workers']
    ADMINS_SHEET = DATA['admins']
    SESSIONS_SHEET = DATA['sessions']
    ORDERS_SHEET = DATA['orders']
    PRODUCTS_SHEET = DATA['products']
    CASH_SHEET = DATA['cash']
except Exception as e:
    print(f'data ОШИБКА ИНИЦИАЛИЗАЦИИ ДАННЫХ - {e}')


def save_data():
    try:
        DATA.save('data/data.xlsx')
        DATA.close()
    except Exception as e:
        print(f'data ОШИБКА СОХРАНЕНИЯ ДАННЫХ - {e}')
