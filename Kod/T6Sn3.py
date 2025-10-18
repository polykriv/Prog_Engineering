from collections import Counter

def top_3_frequent_numbers(s):
    counts = Counter(map(int, s))
    most_common = counts.most_common(3)
    result_dict = dict(sorted(most_common, key=lambda x: x[0]))
    return result_dict

if __name__ == "__main__":
    input_str = input("Введите строку цифр (длина минимум 15): ")
    if len(input_str) < 15 or not input_str.isdigit():
        print("Ошибка: строка должна содержать не менее 15 цифр.")
    else:
        result = top_3_frequent_numbers(input_str)
        print("Три самых частых числа с их количеством:")
        for num in sorted(result.keys()):
            print(f"{num}: {result[num]}")