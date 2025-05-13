import re

DATA_FILE = "D:\\workspace\\data.txt"

def validate_name(name):
    pattern = r"[A-Za-zА-Яа-яЁё]{2,20}(?:-[A-Za-zА-Яа-яЁё]{2,20})*"
    return bool(re.fullmatch(pattern, name, re.UNICODE))

def validate_department(department):
    return bool(re.fullmatch(r"[A-Za-zА-Яа-яЁё0-9]+(?: [A-Za-zА-Яа-яЁё0-9]+)?", department))

def validate_children(children):
    return children.isdigit() and 0 <= int(children) <= 19

def get_valid_input(prompt, validation_func, error_message):
    while True:
        value = input(prompt).strip()
        if validation_func(value):
            return value
        else:
            print(error_message)

def add_employee():
    surname = get_valid_input(
        "Введите фамилию: ",
        validate_name,
        "Фамилия должна содержать только буквы (2–20 символов), можно с одним дефисом."
    )

    name = get_valid_input(
        "Введите имя: ",
        validate_name,
        "Имя должно содержать только буквы (2–20 символов), можно с одним дефисом."
    )

    department = get_valid_input(
        "Введите название отдела: ",
        validate_department,
        "Название отдела должно содержать только буквы/цифры, максимум один пробел."
    ).replace(" ", "_")

    children = get_valid_input(
        "Введите количество детей младше 18 лет: ",
        validate_children,
        "Количество детей должно быть целым числом от 0 до 19."
    )

    try:
        with open(DATA_FILE, "a", encoding="utf-8") as file:
            file.write(f"{surname}\t{name}\t{department}\t{children}\n")
        print("Данные успешно сохранены.\n")
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}\n")

def display_children_data():
    total = 0
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            lines = file.readlines()
            if not lines:
                print("Нет данных для отображения.\n")
                return

            print("Список сотрудников и количество их детей:")
            for line in lines:
                parts = line.strip().split("\t")
                if len(parts) != 4:
                    print(f"Неверный формат строки: {line.strip()}")
                    continue
                surname, name, department, children = parts
                if validate_children(children):
                    print(f"{surname} {name}, отдел: {department}, детей: {children}")
                    total += int(children)
                else:
                    print(f"Некорректное количество детей у {surname} {name}")
            print(f"Общее количество детей: {total}\n")
    except FileNotFoundError:
        print("Файл data.txt не найден.\n")

def show_childless_employees():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            found = False
            print("Сотрудники без детей:")
            for line in file:
                parts = line.strip().split("\t")
                if len(parts) != 4:
                    print(f"Неверный формат строки: {line.strip()}")
                    continue
                surname, name, department, children = parts
                if validate_children(children) and int(children) == 0:
                    print(f"{surname} {name}")
                    found = True
            if not found:
                print("Нет сотрудников без детей.\n")
            else:
                print()
    except FileNotFoundError:
        print("Файл data.txt не найден.\n")
