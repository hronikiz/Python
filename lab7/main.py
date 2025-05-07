from employee_module import add_employee, display_children_data, show_childless_employees

def main():
    while True:
        print("Меню:")
        print("1. Ввод данных о сотруднике")
        print("2. Просмотр данных о детях сотрудников")
        print("3. Список сотрудников без детей")
        print("4. Выход")

        choice = input("Выберите опцию (1-4): ").strip()

        if choice == "1":
            add_employee()
        elif choice == "2":
            display_children_data()
        elif choice == "3":
            show_childless_employees()
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Повторите.\n")

main()
