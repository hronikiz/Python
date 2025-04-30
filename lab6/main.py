def number(number):
    if number.startswith("+373") and len(number) == 12 and number[4:].isdigit():
        return number[4] in "678"  
    elif number.startswith("00373") and len(number) == 13 and number[5:].isdigit():
        return number[5] in "678"
    elif number.startswith("0") and len(number) == 9 and number[1:].isdigit():
        return number[1] in "678"
    elif len(number) == 8 and number.isdigit():
        return number[0] in "678"
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
