import functions as func

shopping_list = []

def menu():
    while True:
        print("\nМеню:")
        print("1. Вывести список текущих товаров")
        print("2. Добавить товар в список")
        print("3. Удалить товар из списка")
        print("4. Выход")
        
        option = input("Выберите опцию (1-4): ")

        if option == '1':
            func.display_list(shopping_list)
        elif option == '2':
            item = input("Введите товар для добавления: ")
            func.add_item(shopping_list, item)
        elif option == '3':
            remove_option = input("Удалить товар по:\n1. Позиции\n2. Названию\nВыберите опцию (1-2): ")
            
            if remove_option == '1':
                try:
                    index = int(input(f"Введите номер товара для удаления (от 1 до {len(shopping_list)}): "))
                    func.remove_item(shopping_list, index=index)
                except ValueError:
                    print("Ошибка: введено неверное значение. Номер должен быть числом.")
            elif remove_option == '2':
                item = input("Введите название товара для удаления: ")
                func.remove_item(shopping_list, item=item)
            else:
                print("Неверный выбор. Попробуйте снова.")
        elif option == '4':
            print("Выход из программы.")
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите опцию от 1 до 4.")

menu()
