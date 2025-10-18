def remove_element_from_tuple(input_tuple, element_to_remove):

    try:
        index_to_remove = input_tuple.index(element_to_remove)
        new_tuple = input_tuple[:index_to_remove] + input_tuple[index_to_remove+1:]
        return new_tuple
    except ValueError:
        return input_tuple

tuple1 = (1, 2, 3, 2, 4)
element1 = 2
result1 = remove_element_from_tuple(tuple1, element1)
print(f"Исходный кортеж: {tuple1}, Удаляем: {element1}, Результат: {result1}")