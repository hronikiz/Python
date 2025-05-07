import re

def is_valid_moldova_phone(number):
    pattern = r'^(\+373\d{8}|00373\d{8}|0\d{8}|\d{8})$'
    return re.fullmatch(pattern, number)

while True:
    try:
        phone = input("Введите номер телефона Молдовы: ").strip()
        
        if is_valid_moldova_phone(phone):
            print(f"Номер принят: {phone}")
            break
        else:
            print("Неверный формат номера. Попробуйте снова.")
    
    except Exception as error:
        print(f"Произошла ошибка: {error}. Пожалуйста, попробуйте снова.")
