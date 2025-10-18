# Тема_6: Базовые коллекции: словари, кортежи

- Студентка: Кривощекова Полина Андреевна
- Группа: ИВТ-23-1

# Выполненные задания
| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |

#Лабораторная работа по Python
## №1
В школе попросили написать программу для учителей, которая по номеру кабинета будет выводить ключ доступа и статус — занят кабинет или нет. Для этого нужно использовать словарь (dict), куда подаётся номер кабинета, а программа выводит соответствующую информацию. Если кабинет в словаре отсутствует, вывести "None" и статус "False". Это упражнение учит замене громоздких условий if/elif/else с помощью словаря.

```  python
request = int(input('Введите номер кабинета: '))

dictionary = {
    101: {'key': 1234, 'access': True},
    102: {'key': 1337, 'access': True},
    103: {'key': 8943, 'access': True},
    104: {'key': 5555, 'access': False},
    None: {'key': None, 'access': False}
}

response = dictionary.get(request)
if not response:
    response = dictionary[None]
key = response.get('key')
access = response.get('access')
print(key, access)
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_5/Screen/1.png)

### Вывод:
Выполнение демонстрирует работу с множествами и операцией разности, позволяя эффективно находить уникальные элементы первого множества.

## №2
Алексей создает функцию dict_maker(**kwargs), которая принимает любое количество параметров «ключ: значение» и обновляет словарь my_dict (с начальными данными {"first": "so easy"}). Это помогает вам понять, как создавать и обновлять словари с произвольным набором ключей и значений.

```
from pprint import pprint

my_dict = {'first': 'so easy'}

def dict_maker(**kwargs):
    my_dict.update(**kwargs)

dict_maker(a1=1, a2=20, a3=54, a4=13)
dict_maker(name='Михаил', age=31, weight=70, eyes_color='голубой')
pprint(my_dict)
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_5/Screen/2.png)

### Вывод:
Показано отличие изменяемого множества set() от неизменяемого frozenset(), где добавление новых элементов в frozenset() невозможно.

## №3
Нужно разложить строку на отдельные символы, используя кортеж (tuple). Для этого берётся любая строка, она "оборачивается" в tuple, что позволяет работать с символами посимвольно, например преобразовать в список или применить другие операции.

```
input_string = 'HelloWorld'
result = tuple(input_string)
print(result)
print(list(result))
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_5/Screen/3.png)

### Вывод:
Реализована замена элементов списка с использованием временной переменной, что поможет освоить базовые операции со списками.

## №4
Вовочка решил сделать функцию, которая принимает на вход кортеж с данными (имя, возраст, место работы) и выводит эту информацию. Задание на работу с кортежами как с параметрами функций.

```
def personal_info(name, age, company = 'unnamed'):
    print(f"Имя: {name} Возраст: {age} Компания: {company}")

tom = ("Григорий", 22)
personal_info(*tom)

bob = ("Георгий", 41, "Yandex")
personal_info(*bob)
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_5/Screen/4.png)

### Вывод:
Использование срезов позволяет легко вывести нужный диапазон элементов из списка без дополнительных циклов.

## №5
Для сопровождения первых лиц нужна функция, которая принимает кортеж из целых чисел и сортирует его по возрастанию. Если хотя бы один элемент не целое число, функция возвращает исходный кортеж без изменений.

```
def tuple_sort(tpl):
    for elm in tpl:
        if not isinstance(elm, int):
            return tpl
    return tuple(sorted(tpl))

if __name__ == '__main__':
    print(tuple_sort((5, 5, 3, 1, 9)))
    print(tuple_sort((5, 5, 2.1, '1', 9)))
```

### Результат
![Меню].(https://github.com/polykriv/Prog_Engineering/blob/Tema_5/Screen/5.png)

### Вывод:
Функция показывает простой способ нахождения отношения максимального значения к длине списка, что может использоваться в разных алгоритмах.

#Самостоятельная работа по Python

## №6
При создании сайта у вас возникла потребность обрабатывать данные пользователя в странной форме, а потом переводить их в нужные форматы. Вы хотите принимать от пользователя последовательность чисел, разделенных пробелом, а после переформатировать эти данные в список и кортеж. Реализуйте программу с использованием input(). Результатом будет выведенный список и кортеж из начальных данных.

```
data = input('Введите последовательность чисел через пробел: ')
list_data = data.split()
tuple_data = tuple(list_data)
print("Список:", list_data)
print("Кортеж:", tuple_data)
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_5/Screen/1(11).png)

### Вывод:
Произведён подсчет посещений и уникальных посетителей ресторана, а также определен самый частый посетитель по данным спискам.

## №7
Николай хочет доказать, что кортежи неизменяемы, и создает функцию, которая удаляет первое появление определенного элемента из кортежа по значению, возвращая изменённый кортеж. Если элемента нет в кортеже, возвращается исходный кортеж. Входные данные и ожидаемые результаты даны.

```
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
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_5/Screen/2(12).png)

### Вывод:
Реализован анализ результатов с сортировкой, нахождением лучших, худших и выделением части данных по индексу.

## №8
Дана строка с последовательностью цифр (0-9), длиной минимум 15 символов. Требуется создать функцию, принимающую строку цифр и возвращающую словарь из 3-х самых частых чисел с количеством их вхождений. Значения словаря нужно вывести в порядке возрастания ключа.

```
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
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_5/Screen/3(13).png)

### Вывод:
Расчет площадей максимального и минимального треугольников по спискам сторон с учетом проверки существования треугольника.

## №9
Напишите функцию, которая принимает кортеж и элемент (id). Нужно вернуть новый кортеж, начиная с первого появления элемента и заканчивая вторым появлением включительно. Если элемент отсутствует — вернуть пустой кортеж, если встречается один раз — вернуть кортеж от этого элемента до конца исходного.

```
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
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_5/Screen/4(14).png)

### Вывод:
Обработка списка оценок с удалением нежелательных значений и заменой некоторых, что полезно для корректировки данных.

## №10
Самостоятельно придумайте задачу с использованием списка или кортежа, решите ее и проведите минимум три теста.

```
def unique_elements_count(lst, threshold):
    unique_count = len(set(lst))
    return unique_count > threshold

def test_task5():
    print(unique_elements_count([1, 2, 3, 2, 1], 5))

    print(unique_elements_count(['a', 'b', 'a', 'c'], 3))

    print(unique_elements_count([], 0))

if __name__ == "__main__":
    test_task5()
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_5/Screen/5(15).png)


### Вывод:
Программа формирует множества с повторяющимися значениями заданного числа, что иллюстрирует работу с подсчетом элементов.

