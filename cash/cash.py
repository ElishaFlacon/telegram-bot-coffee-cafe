from data import *
from datetime import *


# Функция изменения денег в кассе
def change_cash_balance(money, card, option):
    try:
        if option == 'увеличить':
            if card == 'карта' or card == True:
                CASH_SHEET[f'B{2}'] = str(
                    float(money) + float(CASH_SHEET[f'B{2}'].value))
            elif card == 'наличные' or card == False:
                CASH_SHEET[f'A{2}'] = str(
                    float(money) + float(CASH_SHEET[f'A{2}'].value))
        elif option == 'уменьшить':
            if card == 'карта' or card == True:
                CASH_SHEET[f'B{2}'] = str(
                    float(CASH_SHEET[f'B{2}'].value) - float(money))
            elif card == 'наличные' or card == False:
                CASH_SHEET[f'A{2}'] = str(
                    float(CASH_SHEET[f'A{2}'].value) - float(money))
        CASH_SHEET[f'C{2}'] = str(
            float(CASH_SHEET[f'A{2}'].value) + float(CASH_SHEET[f'B{2}'].value))
        CASH_SHEET[f'D{2}'] = str(datetime.now())[:-7]
        save_data()
    except Exception as e:
        print(f'cash Строка №29 - {e}')


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


# Функция выводит количество денег в кассе
def get_cash_value():
    return f'Наличные : {CASH_SHEET[f"A2"].value} р.\nКартой: {CASH_SHEET[f"B2"].value} р.\nОбщие: {CASH_SHEET[f"C2"].value} р.\nВермя последнего обновления кассы: {CASH_SHEET[f"D2"].value}'
