import re

def valid(number):
    pattern = r'^(\+373|00373|0)?\d{8}$'
    return re.fullmatch(pattern, number) is not None

while True:
    try:
        phone = input("Введите номер телефона Молдовы: ")
        if valid(phone):
            print(f"Номер принят: {phone}")
            break
        else:
            raise ValueError("Неверный формат номера телефона.")
    except ValueError as ve:
        print(ve)
