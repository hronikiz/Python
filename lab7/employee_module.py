import re

DATA_FILE = "D:\workspace\data.txt"

def validate_name(name):
    # Проверка: от 2 до 20 символов, только кириллица или латиница, можно несколько дефисов
    pattern = r"[A-Za-zА-Яа-яЁё]{2,20}(?:-[A-Za-zА-Яа-яЁё]{2,20})*"
    return bool(re.fullmatch(pattern, name, re.UNICODE))

def validate_department(department):
    # Отдел должен содержать только буквы и цифры, и один пробел, максимум
    return bool(re.fullmatch(r"[A-Za-zА-Яа-яЁё0-9]+(?: [A-Za-zА-Яа-яЁё0-9]+)*", department))

def validate_children(children):
    # Кол-во детей: целое число от 0 до 19
    return children.isdigit() and 0 <= int(children) <= 19

def add_employee():
    while True:
        surname = input("Введите фамилию: ").strip()
        name = input("Введите имя: ").strip()
        department = input("Введите название отдела: ").strip()
        children = input("Введите количество детей младше 18 лет: ").strip()

        if (validate_name(surname) and validate_name(name) and
            validate_department(department) and validate_children(children)):
            department = department.replace(" ", "_")
            try:
                with open(DATA_FILE, "a", encoding="utf-8") as file:
                    file.write(f"{surname}\t{name}\t{department}\t{children}\n")
                print("Данные успешно сохранены.\n")
            except Exception as e:
                print(f"Ошибка при записи в файл: {e}\n")
            break
        else:
            print("Ошибка ввода! Убедитесь, что:")
            print("- Фамилия и имя содержат только буквы (2–20 символов), можно с одним дефисом")
            print("- Название отдела содержит буквы/цифры, максимум один пробел")
            print("- Количество детей — число от 0 до 19\n")

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
                surname, name, department, children = line.strip().split("\t")
                print(f"{surname} {name}, отдел: {department}, детей: {children}")
                total += int(children)
            print(f"Общее количество детей: {total}\n")
    except FileNotFoundError:
        print("Файл data.txt не найден.\n")

def show_childless_employees():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            found = False
            print("Сотрудники без детей:")
            for line in file:
                surname, name, department, children = line.strip().split("\t")
                if int(children) == 0:
                    print(f"{surname} {name}")
                    found = True
            if not found:
                print("Нет сотрудников без детей.\n")
            else:
                print()
    except FileNotFoundError:
        print("Файл data.txt не найден.\n")
