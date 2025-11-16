class NegativeNumberError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Отрицательное число не допускается: {value}")

def validate_positive_number(number):
    if number < 0:
        raise NegativeNumberError(number)
    return number

def calculate_square_root(number):
    try:
        validated_number = validate_positive_number(number)
        result = validated_number ** 0.5
        print(f"Квадратный корень из {number} = {result:.2f}")
        return result
    except NegativeNumberError as e:
        print(f"Ошибка: {e}")

def process_age(age):
    try:
        validate_positive_number(age)
        print(f"Возраст {age} корректен")
    except NegativeNumberError as e:
        print(f"Ошибка в возрасте: {e}")

if __name__ == '__main__':
    calculate_square_root(25)
    calculate_square_root(-9)  # Вызовет исключение
    process_age(30)
    process_age(-5)  # Вызовет исключение