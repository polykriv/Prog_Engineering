import json

filename = "expenses.json"
categories = ["еда", "одежда", "лекарства", "отдых", "коммунальные услуги"]

def load_expenses():
    try:
        with open(filename, "r", encoding="utf-8") as f:
            # Защита от пустого файла
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_expenses(expenses):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(expenses, f, indent=2, ensure_ascii=False)

def add_expense():
    print("Категории:", ", ".join(categories))
    category = input("Категория расхода: ").lower()
    if category not in categories:
        print("Неверная категория!")
        return
    try:
        amount = float(input("Сумма: "))
    except ValueError:
        print("Неправильный ввод суммы")
        return
    expenses.append({"Категория": category, "Сумма": amount})
    save_expenses(expenses)
    print("Расход добавлен.")

def show_expenses():
    if not expenses:
        print("Расходы отсутствуют")
    for e in expenses:
        print(f"{e.get('Категория', 'неизвестно')}: {e.get('Сумма', 0)}")

expenses = load_expenses()

while True:
    action = input("Введите '+' для добавления, 'смотреть' для просмотра, '->' для выхода: ").lower()
    if action == "+":
        add_expense()
    elif action == "смотреть":
        show_expenses()
    elif action == "->":
        print("Выход из программы.")
        break
    else:
        print("Неверная команда, попробуйте снова.")