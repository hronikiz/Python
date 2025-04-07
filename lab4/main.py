
def main():
    while True:
        try:
            height = int(input("Введите ваш рост (150 – 220 см): "))
            if 150 <= height <= 220:
                break  
            else:
                print("Ошибка: рост должен быть от 150 до 220 см.")
        except ValueError:
            print("Ошибка: введите целое число.")

    while True:
        try:
            age = int(input("Введите ваш возраст (18 – 120 лет): "))
            if 18 <= age <= 120:
                break  
            else:
                print("Ошибка: возраст должен быть от 18 до 120 лет.")
        except ValueError:
            print("Ошибка: введите целое число.")

    while True:
        try:
            weight = float(input("Введите ваш вес (45 - 300 кг): "))
            if 45 <= weight <= 300:
                break
            else:
                print("Ошибка: вес должен быть от 45 до 300 кг.")
        except ValueError:
            print("Ошибка: введите число.")

    while True:
        try:
            gender = input("Введите ваш пол (М/Ж): ").strip().upper()
            if gender in ["М", "Ж"]:
                break
            else:
                print("Ошибка: пол должен быть 'М' или 'Ж'.")
        except ValueError:
            print("Ошибка: введите 'М' или 'Ж'.")

    calculate_ideal_weight(gender, height, age, weight)

def calculate_ideal_weight(gender, height, age, weight):
    if gender == "М":
        ideal_weight = height - 100 - (height - 150) / 4 + (age - 20) / 4 
    elif gender == "Ж":
        ideal_weight = height - 110 - (height - 150) / 2.5 + (age - 20) / 6
    else:
        raise ValueError("Некорректный пол")
    print(f"Ваш текущий вес: {weight:.2f} кг.")
    print(f"Ваш идеальный вес: {ideal_weight:.2f} кг.")

    difference = weight - ideal_weight
    if difference > 0:
        print(f"У вас избыточный вес на {difference:.2f} кг.")
    elif difference < 0:
        print(f"У вас недостаточный вес на {abs(difference):.2f} кг.")
    else:
        print("Ваш вес идеален.")
    return ideal_weight

main() 

cat_to_human_months = {
    1: "6 месяцев",
    2: "10 месяцев",
    3: "2 года",
    4: "5 лет",
    5: "8 лет",
    6: "14 лет",
    7: "15 лет",
    8: "16 лет",
    9: "16 лет",
    10: "17 лет",
    11: "17 лет"
}

def get_yes_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ["да", "нет", "yes", "no"]:
            return answer
        print("Пожалуйста, введите Да/Нет.")

def get_year_word(n):
    if 11 <= n % 100 <= 14:
        return "лет"
    elif n % 10 == 1:
        return "год"
    elif 2 <= n % 10 <= 4:
        return "года"
    else:
        return "лет"

young_cat = get_yes_no("Кошке меньше года? (Да/Нет): ")

if young_cat in ["да", "yes"]:
    while True:
        try:
            months = int(input("Введите возраст кошки в месяцах (от 1 до 11): "))
            if 1 <= months <= 11:
                print(f"Возраст кошки в человеческих годах: {cat_to_human_months[months]}")
                break
            else:
                print("Введите число от 1 до 11.")
        except ValueError:
            print("Пожалуйста, введите корректное число.")
else:
    while True:
        try:
            years = int(input("Введите возраст кошки в годах (от 1 до 35): "))
            if 1 <= years <= 35:
                if years == 1:
                    human_age = 18
                elif years == 2:
                    human_age = 25
                elif 3 <= years <= 15:
                    human_age = 25 + (years - 2) * 4
                else:  
                    human_age = 25 + (13 * 4) + (years - 15) * 3
                print(f"Возраст кошки в человеческих годах: {human_age} {get_year_word(human_age)}")
                break
            else:
                print("Возраст должен быть от 1 до 35 лет.")
        except ValueError:
            print("Пожалуйста, введите корректное число.")
