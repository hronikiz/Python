import datetime
import calendar
import math
import time
import tkinter as tk
from tkinter import messagebox

# Задание 1: Рассчитать возраст в днях
def calculate_age_in_days():
    today = datetime.date.today()
    year = int(input("Год рождения: "))
    month = int(input("Месяц рождения: "))
    day = int(input("День рождения: "))
    
    birth_date = datetime.date(year, month, day)
    age_in_days = (today - birth_date).days
    print(f"Вы прожили {age_in_days} дней.")

# Задание 2: Определить день недели по дате
def day_of_week():
    year = int(input("Введите год: "))
    month = int(input("Введите месяц: "))
    day = int(input("Введите день: "))
    
    day_number = calendar.weekday(year, month, day)
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    print(f"Это был {days[day_number]}")

# Задание 3: Расчёт времени падения объекта
def fall_time():
    h = float(input("Введите высоту в метрах: "))
    g = 9.8
    t = math.sqrt((2 * h) / g)
    print(f"Время падения: {round(t, 2)} секунд")

# Задание 4: Таймер для медитации (с использованием tkinter и time)
def meditation_timer():
    def start_timer():
        minutes = int(entry.get())
        seconds = minutes * 60
        while seconds:
            minutes, seconds = divmod(seconds, 60)
            time_str = f'{minutes:02}:{seconds:02}'
            label.config(text=time_str)
            window.update()
            time.sleep(1)
            seconds -= 1
        messagebox.showinfo("Таймер", "Время медитации завершено!")

    window = tk.Tk()
    window.title("Таймер для медитации")
    
    label = tk.Label(window, text="00:00", font=("Helvetica", 48))
    label.pack()
    
    entry_label = tk.Label(window, text="Введите количество минут: ")
    entry_label.pack()
    
    entry = tk.Entry(window)
    entry.pack()
    
    start_button = tk.Button(window, text="Начать", command=start_timer)
    start_button.pack()
    
    window.mainloop()

# Выбор задания для выполнения
def main():
    print("Выберите задание:")
    print("1. Рассчитать возраст в днях")
    print("2. Определить день недели по дате")
    print("3. Расчёт времени падения объекта")
    print("4. Таймер для медитации")

    choice = int(input("Введите номер задания: "))
    
    if choice == 1:
        calculate_age_in_days()
    elif choice == 2:
        day_of_week()
    elif choice == 3:
        fall_time()
    elif choice == 4:
        meditation_timer()
    else:
        print("Неверный выбор!")

if __name__ == "__main__":
    main()
