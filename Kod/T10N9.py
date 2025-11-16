def cache_decorator(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            print(f"Результат взят из кэша для аргументов {args}")
            return cache[args]
        result = func(*args)
        cache[args] = result
        print(f"Результат вычислен и сохранен в кэш для аргументов {args}")
        return result

    return wrapper


@cache_decorator
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


@cache_decorator
def power_of_two(n):
    return 2 ** n


if __name__ == '__main__':
    print("Факториал 5:", factorial(5))
    print("Факториал 5:", factorial(5))
    print("2 в степени 3:", power_of_two(3))
    print("2 в степени 3:", power_of_two(3))
    print("Факториал 3:", factorial(3))