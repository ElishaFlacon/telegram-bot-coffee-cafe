from data import *
from datetime import *


# Функция добовления денег в кассу
def append_money_to_cash(money, card):
    if card:
        CASH_SHEET[f'A{2}'] = str(int(money) + int(CASH_SHEET[f'A{2}'].value))
    elif card == False:
        CASH_SHEET[f'B{2}'] = str(int(money) + int(CASH_SHEET[f'B{2}'].value))
    CASH_SHEET[f'C{2}'] = str(
        int(CASH_SHEET[f'A{2}'].value) + int(CASH_SHEET[f'B{2}'].value))
    CASH_SHEET[f'D{2}'] = str(datetime.now())[:-7]
    save_data()


# Функция удаления денег из кассы
def delete_money_to_cash(money, card):
    if card:
        CASH_SHEET[f'A{2}'] = str(int(money) - int(CASH_SHEET[f'A{2}'].value))
    elif card == False:
        CASH_SHEET[f'B{2}'] = str(int(money) - int(CASH_SHEET[f'B{2}'].value))
    CASH_SHEET[f'C{2}'] = str(
        int(CASH_SHEET[f'A{2}'].value) - int(CASH_SHEET[f'B{2}'].value))
    CASH_SHEET[f'D{2}'] = str(datetime.now())[:-7]
    save_data()


# Функция очистки кассы полностью
def delete_money_to_cash():
    CASH_SHEET[f'A{2}'] = '0'
    CASH_SHEET[f'B{2}'] = '0'
    CASH_SHEET[f'C{2}'] = '0'
    CASH_SHEET[f'D{2}'] = str(datetime.now())[:-7]
    save_data()
