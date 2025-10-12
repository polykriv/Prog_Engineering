def create_set_with_duplicates(data_list):

    counts = {}
    for num in data_list:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    result_set = set()
    for num, count in counts.items():
        result_set.add(num)

        for i in range(2, count + 1):
            result_set.add(str(num) * i)

    return result_set


# Тестовые данные
list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

set_1 = create_set_with_duplicates(list_1)
set_2 = create_set_with_duplicates(list_2)
set_3 = create_set_with_duplicates(list_3)

print("Множество 1:", set_1)
print("Множество 2:", set_2)
print("Множество 3:", set_3)