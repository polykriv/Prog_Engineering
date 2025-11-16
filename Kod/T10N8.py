def add_two():
    try:
        user_input = input("Введите число для сложения с 2: ")
        number = float(user_input)
        result = 2 + number
        print(f"Результат: 2 + {number} = {result}")
    except ValueError:
        print("Неподходящий тип данных. Ожидалось число.")

if __name__ == '__main__':
    add_two()
    add_two()
    add_two()