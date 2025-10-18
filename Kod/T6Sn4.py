def tuple_subrange(tpl, element):
    if element not in tpl:
        return ()
    first_idx = tpl.index(element)
    try:
        second_idx = tpl.index(element, first_idx + 1)
        return tpl[first_idx:second_idx+1]
    except ValueError:
        return tpl[first_idx:]

if __name__ == "__main__":
    input_str = input("Введите элементы кортежа через пробел: ")
    tuple_data = tuple(input_str.split())

    element = input("Введите элемент для поиска: ")

    result = tuple_subrange(tuple_data, element)
    print("Результат:", result)
