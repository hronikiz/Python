from employee import Employee, HourlyEmployee, SalaryEmployee, input_employee_data

def input_float(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Ошибка: введите число!\n")

def main():
    print("=== Ввод данных для обычных сотрудников ===")
    print("\nСотрудник 1:")
    name, phone, bday, email, position = input_employee_data()
    employee1 = Employee(name, phone, bday, email, position)

    print("\nСотрудник 2:")
    name, phone, bday, email, position = input_employee_data()
    employee2 = Employee(name, phone, bday, email, position)

    print("\n=== Ввод данных для почасовых сотрудников ===")
    print("\nПочасовой сотрудник 1:")
    name, phone, bday, email, position = input_employee_data()
    nmbrOfHour = input_float("Введите количество отработанных часов: ")
    hourlyPay = input_float("Введите оплату за час: ")
    hourly_employee1 = HourlyEmployee(name, phone, bday, email, position, nmbrOfHour, hourlyPay)

    print("\nПочасовой сотрудник 2:")
    name, phone, bday, email, position = input_employee_data()
    nmbrOfHour = input_float("Введите количество отработанных часов: ")
    hourlyPay = input_float("Введите оплату за час: ")
    hourly_employee2 = HourlyEmployee(name, phone, bday, email, position, nmbrOfHour, hourlyPay)

    print("\n=== Ввод данных для сотрудников с фиксированной зарплатой ===")
    print("\nСотрудник с фикс. зарплатой 1:")
    name, phone, bday, email, position = input_employee_data()
    salary = input_float("Введите ежемесячную зарплату: ")
    salary_employee1 = SalaryEmployee(name, phone, bday, email, position, salary)

    print("\nСотрудник с фикс. зарплатой 2:")
    name, phone, bday, email, position = input_employee_data()
    salary = input_float("Введите ежемесячную зарплату: ")
    salary_employee2 = SalaryEmployee(name, phone, bday, email, position, salary)

    print("\n" + "="*40)
    print("     🧾 Информация о сотрудниках")
    print("="*40)

    def print_employee(emp, title, salary_info=None):
        print(f"\n--- {title} ---")
        print(f"ФИО: {emp.nameEmployee}")
        print(f"Телефон: {emp.phone}")
        print(f"Дата рождения: {emp.bday}")
        print(f"Email: {emp.email}")
        print(f"Должность: {emp.position}")
        print(f"Возраст: {emp.calculateAge()} лет")
        if salary_info:
            print(salary_info)

    print_employee(employee1, "Обычный сотрудник 1")
    print_employee(employee2, "Обычный сотрудник 2")

    print_employee(hourly_employee1, "Почасовой сотрудник 1",
                   f"Отработано часов: {hourly_employee1.nmbrOfHour}\n"
                   f"Ставка за час: {hourly_employee1.hourlyPay}\n"
                   f"Зарплата: {hourly_employee1._calculateSalary()}")

    print_employee(hourly_employee2, "Почасовой сотрудник 2",
                   f"Отработано часов: {hourly_employee2.nmbrOfHour}\n"
                   f"Ставка за час: {hourly_employee2.hourlyPay}\n"
                   f"Зарплата: {hourly_employee2._calculateSalary()}")

    print_employee(salary_employee1, "Сотрудник с фикс. зарплатой 1",
                   f"Месячная зарплата: {salary_employee1._calculateSalary()}")

    print_employee(salary_employee2, "Сотрудник с фикс. зарплатой 2",
                   f"Месячная зарплата: {salary_employee2._calculateSalary()}")

    print("\n" + "="*40)
    print("        💰 Зарплаты сотрудников")
    print("="*40)

    print("\nПочасовые сотрудники:")
    print(f"1. {hourly_employee1.nameEmployee} — {hourly_employee1._calculateSalary()} ед.")
    print(f"2. {hourly_employee2.nameEmployee} — {hourly_employee2._calculateSalary()} ед.")

    print("\nСотрудники с фиксированной зарплатой:")
    print(f"1. {salary_employee1.nameEmployee} — {salary_employee1._calculateSalary()} ед.")
    print(f"2. {salary_employee2.nameEmployee} — {salary_employee2._calculateSalary()} ед.")

if __name__ == "__main__":
    main()
