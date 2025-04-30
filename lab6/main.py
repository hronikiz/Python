import re

def is_valid_phone(number):
    pattern = r'^(\+373|00373|0)?\d{8}$'
    return re.fullmatch(pattern, number) is not None

while True:
    try:
        phone = input("Введите номер телефона Молдовы: ")
        if is_valid_phone(phone):
            print(f"Номер принят: {phone}")
            break
        else:
            raise ValueError("Неверный формат номера телефона.")
    except ValueError as ve:
        print(ve)
