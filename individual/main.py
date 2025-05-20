import json
import os


class RecipeGenerator:
    def __init__(self, file_path="recipes.json"):
        self.file_path = file_path
        self.recipes = self.load_recipes()

    def load_recipes(self):
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print("Ошибка чтения файла. Создан новый список рецептов.")
        return {}

    def save_recipes(self):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(self.recipes, f, ensure_ascii=False, indent=4)

    def add_recipe(self):
        name = input("Название рецепта: ").strip()
        if not name:
            print("Название не может быть пустым.")
            return
        if name in self.recipes:
            if input("Рецепт уже существует. Перезаписать? (да/нет): ").lower() != "да":
                return

        ingredients = {}
        print("Введите ингредиенты (пустая строка — завершение):")
        while True:
            ing = input("Ингредиент: ").strip()
            if not ing:
                break
            qty = input("Количество: ").strip()
            ingredients[ing] = qty or "по вкусу"

        if not ingredients:
            print("Нет ингредиентов!")
            return

        description = input("Описание приготовления: ").strip()
        self.recipes[name] = {"ingredients": ingredients, "description": description}
        self.save_recipes()
        print("Рецепт добавлен.")

    def show_recipes(self, filtered=None):
        recipes = filtered if filtered is not None else list(self.recipes)
        if not recipes:
            print("Нет подходящих рецептов.")
            return

        for i, name in enumerate(recipes, 1):
            print(f"{i}. {name}")

        choice = input("Введите номер для деталей (или 0 для выхода): ")
        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(recipes):
                self.show_details(recipes[idx - 1])

    def show_details(self, name):
        recipe = self.recipes.get(name)
        if not recipe:
            print("Рецепт не найден.")
            return
        print(f"\n=== {name.upper()} ===")
        print("Ингредиенты:")
        for ing, qty in recipe["ingredients"].items():
            print(f"- {ing}: {qty}")
        print("\nПриготовление:")
        print(recipe["description"])
        print("=" * 40)

    def find_by_ingredients(self):
        if not self.recipes:
            print("Нет рецептов.")
            return

        print("Введите свои ингредиенты (пустая строка — завершение):")
        available = set()
        while True:
            ing = input("Ингредиент: ").strip().lower()
            if not ing:
                break
            available.add(ing)

        exact = []
        partial = []

        for name, data in self.recipes.items():
            recipe_ings = {i.lower() for i in data["ingredients"]}
            missing = recipe_ings - available
            if not missing:
                exact.append(name)
            elif len(missing) <= 2:
                partial.append((name, missing))

        print("\nМожно приготовить:")
        self.show_recipes(exact)

        if partial:
            print("\nПочти подходит (не хватает 1-2 ингредиентов):")
            for i, (name, miss) in enumerate(partial, 1):
                print(f"{i}. {name} (не хватает: {', '.join(miss)})")
            choice = input("Введите номер для деталей (или 0 для выхода): ")
            if choice.isdigit():
                idx = int(choice)
                if 1 <= idx <= len(partial):
                    self.show_details(partial[idx - 1][0])


def main():
    rg = RecipeGenerator()
    while True:
        print("\n=== ГЕНЕРАТОР РЕЦЕПТОВ ===")
        print("1. Добавить рецепт")
        print("2. Показать все рецепты")
        print("3. Поиск по ингредиентам")
        print("0. Выход")
        cmd = input("Выбор: ")

        if cmd == "1":
            rg.add_recipe()
        elif cmd == "2":
            rg.show_recipes()
        elif cmd == "3":
            rg.find_by_ingredients()
        elif cmd == "0":
            print("До свидания!")
            break
        else:
            print("Неверный ввод!")


if __name__ == "__main__":
    main()
