def number(number):
    if number.startswith("+373") and len(number) == 12 and number[4:].isdigit():
        return True
    elif number.startswith("00373") and len(number) == 13 and number[5:].isdigit():
        return True
    elif number.startswith("0") and len(number) == 9 and number[1:].isdigit():
        return True
    elif len(number) == 8 and number.isdigit():
        return True
    else:
        return False

while True:
    try:
        phone = input("Введите номер телефона Молдовы: ")
        if number(phone):
            print(f"Номер принят: {phone}")
            break
        else:
            raise ValueError("Неверный формат номера телефона. Попробуйте снова.")
    except ValueError as e:
        print(e)
