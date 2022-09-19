from data import *
from datetime import *


# Функция добовления денег в кассу
def append_money_to_cash(money, card):
    try:
        if card:
            CASH_SHEET[f'A{2}'] = str(
                float(money) + float(CASH_SHEET[f'A{2}'].value))
        elif card == False:
            CASH_SHEET[f'B{2}'] = str(
                float(money) + float(CASH_SHEET[f'B{2}'].value))
        CASH_SHEET[f'C{2}'] = str(
            float(CASH_SHEET[f'A{2}'].value) + float(CASH_SHEET[f'B{2}'].value))
        CASH_SHEET[f'D{2}'] = str(datetime.now())[:-7]
        save_data()
    except Exception as e:
        print(f'cash Строка №19 - {e}')


# Функция удаления денег из кассы
def delete_money_to_cash(money, card):
    try:
        if card:
            CASH_SHEET[f'A{2}'] = str(
                float(money) - float(CASH_SHEET[f'A{2}'].value))
        elif card == False:
            CASH_SHEET[f'B{2}'] = str(
                float(money) - float(CASH_SHEET[f'B{2}'].value))
        CASH_SHEET[f'C{2}'] = str(
            float(CASH_SHEET[f'A{2}'].value) - float(CASH_SHEET[f'B{2}'].value))
        CASH_SHEET[f'D{2}'] = str(datetime.now())[:-7]
        save_data()
    except Exception as e:
        print(f'cash Строка №36 - {e}')


# Функция очистки кассы полностью
def delete_money_to_cash():
    try:
        CASH_SHEET[f'A{2}'] = '0'
        CASH_SHEET[f'B{2}'] = '0'
        CASH_SHEET[f'C{2}'] = '0'
        CASH_SHEET[f'D{2}'] = str(datetime.now())[:-7]
        save_data()
    except Exception as e:
        print(f'cash Строка №48 - {e}')
