# Функция для добавления товара в список
def add_item(shopping_list, item):
    if item in shopping_list:
        print(f"Товар '{item}' уже есть в списке.")
    else:
        shopping_list.append(item)
        print(f"Товар '{item}' добавлен в список.")

# Функция для удаления товара из списка
def remove_item(shopping_list, item=None, index=None):
    if index is not None:
        if index < 1 or index > len(shopping_list):
            print("Некорректный индекс. Попробуйте снова.")
        else:
            removed_item = shopping_list.pop(index - 1)
            print(f"Товар '{removed_item}' удален из списка.")
    elif item is not None:
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"Товар '{item}' удален из списка.")
        else:
            print(f"Товар '{item}' не найден в списке.")
    else:
        print("Не указаны данные для удаления.")

# Функция для вывода списка товаров
def display_list(shopping_list):
    if not shopping_list:
        print("Список покупок пуст.")
    else:
        print("Список покупок:")
        for idx, item in enumerate(shopping_list, 1):
            print(f"{idx}. {item}")
