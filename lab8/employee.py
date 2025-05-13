import re
from datetime import datetime

class Employee:
    def __init__(self, nameEmployee, phone, bday, email, position):
        self.nameEmployee = nameEmployee
        self.phone = phone
        self.bday = bday
        self.email = email
        self.position = position

    @property
    def nameEmployee(self):
        return self.__nameEmployee

    @nameEmployee.setter
    def nameEmployee(self, value):
        if not re.match(r"^[A-Za-zА-Яа-яёЁ\s-]+$", value):
            raise ValueError("Имя должно содержать только буквы.")
        self.__nameEmployee = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        if not isinstance(value, str):
            raise TypeError("Номер телефона должен быть строкой.")
        if not re.match(r"^\+373\d{8}$", value):
            raise ValueError("Номер телефона должен быть в формате +373xxxxxxxx.")
        self.__phone = value

    @property
    def bday(self):
        return self.__bday

    @bday.setter
    def bday(self, value):
        try:
            datetime.strptime(value, "%d.%m.%Y")
        except ValueError:
            raise ValueError("Дата должна быть в формате дд.мм.гггг.")
        self.__bday = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if not re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", value):
            raise ValueError("Некорректный формат email.")
        self.__email = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not re.match(r"^[A-Za-zА-Яа-яёЁ\s-]+$", value):
            raise ValueError("Должность должна содержать только буквы.")
        self.__position = value

    def calculateAge(self):
        birth_date = datetime.strptime(self.__bday, "%d.%m.%Y")
        today = datetime.today()
        return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    def _calculateSalary(self):
        pass


class HourlyEmployee(Employee):
    def __init__(self, nameEmployee, phone, bday, email, position, nmbrOfHour, hourlyPay):
        super().__init__(nameEmployee, phone, bday, email, position)
        self.nmbrOfHour = nmbrOfHour
        self.hourlyPay = hourlyPay

    @property
    def nmbrOfHour(self):
        return self.__nmbrOfHour

    @nmbrOfHour.setter
    def nmbrOfHour(self, value):
        if value < 0:
            raise ValueError("Количество часов не может быть отрицательным.")
        self.__nmbrOfHour = value

    @property
    def hourlyPay(self):
        return self.__hourlyPay

    @hourlyPay.setter
    def hourlyPay(self, value):
        if value < 0:
            raise ValueError("Почасовая ставка не может быть отрицательной.")
        self.__hourlyPay = value

    def _calculateSalary(self):
        return self.__nmbrOfHour * self.__hourlyPay


class SalaryEmployee(Employee):
    def __init__(self, nameEmployee, phone, bday, email, position, salary):
        super().__init__(nameEmployee, phone, bday, email, position)
        self.salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Зарплата не может быть отрицательной.")
        self.__salary = value

    def _calculateSalary(self):
        return self.__salary


def input_employee_data():
    while True:
        try:
            name = input("Введите ФИО (только буквы): ")
            if not re.match(r"^[A-Za-zА-Яа-яёЁ\s-]+$", name):
                raise ValueError("Имя должно содержать только буквы.")
            break
        except ValueError as e:
            print("Ошибка:", e)

    while True:
        try:
            phone = input("Введите номер телефона (+373 и 8 цифр): ")
            if not re.match(r"^\+373\d{8}$", phone):
                raise ValueError("Телефон должен быть в формате +373xxxxxxxx.")
            break
        except ValueError as e:
            print("Ошибка:", e)

    while True:
        try:
            bday = input("Введите дату рождения (дд.мм.гггг): ")
            datetime.strptime(bday, "%d.%m.%Y")
            break
        except ValueError:
            print("Ошибка: неверный формат даты. Используйте дд.мм.гггг.")

    while True:
        try:
            email = input("Введите email: ")
            if not re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", email):
                raise ValueError("Неверный формат email.")
            break
        except ValueError as e:
            print("Ошибка:", e)

    while True:
        try:
            position = input("Введите должность (только буквы): ")
            if not re.match(r"^[A-Za-zА-Яа-яёЁ\s-]+$", position):
                raise ValueError("Должность должна содержать только буквы.")
            break
        except ValueError as e:
            print("Ошибка:", e)

    return name, phone, bday, email, position
