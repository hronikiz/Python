numbers = [10, 20, 30, 40, 50]

print("Первый элемент:", numbers[0])
print("Третий элемент:", numbers[2])

numbers[1] = 25
print("Обновленный список:", numbers)

print("Срез (первые три элемента):", numbers[:3])

numbers.append(60)
print("После добавления элемента:", numbers)

print("Длина списка:", len(numbers))
print("Сумма элементов:", sum(numbers))

print("Есть ли число 30 в списке?", 30 in numbers)  
new_numbers = numbers + [70, 80]  
print("Объединенный список:", new_numbers)  
print("Дублированный список:", numbers * 2)  


data_tuple = (5, 15, 25, 35, 45)

print("Тип данных:", type(data_tuple))

print("Первый элемент:", data_tuple[0])
print("Последний элемент:", data_tuple[-1])

print("Срез (со второго по четвертый):", data_tuple[1:4])

print("Длина кортежа:", len(data_tuple))
print("Сумма элементов:", sum(data_tuple))
print("Максимальный элемент:", max(data_tuple))

numbers_set = {10, 20, 30, 40, 50, 20, 30, 10}

print("Элементы множества:", numbers_set)

numbers_set.add(60)
print("После добавления 60:", numbers_set)

print("Количество элементов в множестве:", len(numbers_set))


text_dict = {
    "имя": "Алексей",
    "город": "Кишинёв",
    "возраст": 25
}

num_dict = {
    1: "один",
    2: "два",
    3: "три"
}

print("Имя:", text_dict["имя"])
print("Город:", text_dict["город"])

print("Число 1:", num_dict[1])
print("Число 2:", num_dict[2])

print("Возраст через get():", text_dict.get("возраст", "Не указано"))
text_dict.update({"возраст": 26, "страна": "Молдова"})
print("Обновленный словарь:", text_dict)
deleted_value = num_dict.pop(3)
print("Удаленное значение:", deleted_value)
print("Словарь после удаления:", num_dict)

print("Количество элементов в text_dict:", len(text_dict))
print("Отсортированные ключи num_dict:", sorted(num_dict))


numbers_tuple = (5, 15, 25)
numbers_list = list(numbers_tuple)
numbers_list.append(35)  

print("Исходный кортеж:", numbers_tuple)
print("Преобразованный список:", numbers_list)

-------------------------------------------------------------

prices = [150, 300, 500]

products = ["Кофе", "Чай", "Шоколад"]

info1 = "Товар: {} | Цена: {} леев".format(products[0], prices[0])
info2 = "Товар: {} | Цена: {} леев".format(products[1], prices[1])
info3 = "Товар: {} | Цена: {} леев".format(products[2], prices[2])

print(info1)
print(info2)
print(info3)


age = int(input("Введите ваш возраст: "))

future_age = age + 5

print("Через 5 лет вам будет " + str(future_age) + " лет.")

products = ["Кофе", "Чай", "Шоколад"]

if "Чай" in products:
    print("Чай есть в списке товаров!")
else:
    print("Чая нет в списке товаров.")

if "Молоко" not in products:
    print("Молоко отсутствует в списке товаров.")




