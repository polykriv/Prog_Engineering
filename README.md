# Тема_4: Функции и модули

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
| Задание 6 | + |   |
| Задание 7 | + |   |
| Задание 8 | + |   |
| Задание 9 | + |   |
| Задание 10 | + |   |

#Лабораторная работа по Python
## №1
Выведите в консоль три строки. Первая – любое число. Вторая – любое число в виде строки. Третья – любое число с плавающей точкой.

```  python
def main():
    print(2+2)

if __name__ == '__main__':
    main()
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_3/ScreenKod/1.png)

### Вывод:


## №2
Выведите в консоль три строки. Первая – результат сложения или вычитания минимум двух переменных типа int. Вторая – результат сложения или вычитания минимум двух переменных типа float. Третья – результат сложения или вычитания минимум двух переменных типа int и float.

```
def main():
    result = 2 + 2
    return result

if __name__ == '__main__':
    answer = main()
    print(answer)
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_3/ScreenKod/2.png)

### Вывод:


## №3
Выведите в консоль три строки. Первая – обычная строка. Вторая – F строка с использованием заранее объявленной переменной. Третья – сложите две или более строк в одну.

```
def main(one, two):
    result = one + two
    return result

for i in range(5):
    x = 1
    y = 10
    answer = main(x, y)
    print(answer)
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_3/ScreenKod/3.png)

### Вывод:


## №4
Выведите в консоль три строки. Первая - трансформация любого типа переменной в bool.
Вторая - трансформация любого типа переменной в float или int. Третья - трансформация любого типа переменной в str. 

```
def main(x, *args):
    one = x
    two = sum(args)
    three = float(len(args))

    print(f"one={one}\ntwo={two}\nthree={three}")

    return x + sum(args) / float(len(args))

if __name__ == '__main__':
    result = main(10, 0, 1, 2, -1, 0, -1, 1, 2)
    print(f"\nresult={result}")
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_3/ScreenKod/4.png)

### Вывод:


## №5
 Присвойте трем переменным различные значения, воспользовавшись функцией input()

```
def main(**kwargs):
    for i in kwargs.items():
        print(i[0], i[1])

    print()

    for key in kwargs:
        print(f"{key} = {kwargs[key]}")

if __name__ == '__main__':
    main(x=[1, 2, 3], y=[3, 3, 0], z=[2, 3, 0], q=[3, 3, 0], w=[3, 3, 0])
    print()

    main(**{'x': [1, 2, 3], 'y': [3, 3, 0]})
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_3/ScreenKod/5.png)

### Вывод:


## №6
Создайте две любые числовые переменные и выполните над ними несколько математических операций: возведение в степень, обычное деление, целочисленное деление, нахождение остатка от деления. При желании вы можете проверить как работают эти вычисления с разными типами данных, например, сначала создать две переменные int, затем создать две переменные float и наконец создать переменные типа int и float и провести над ними операции, прописанные выше

```
def main(**kwargs):

    for i, j in kwargs.items():
        print(f"{i}. Mean = {mean(j)}")

def mean(data):
    return sum(data) / float(len(data))

if __name__ == "__main__":
    main(x=[1, 2, 3], y=[3, 3, 0])
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_3/ScreenKod/6.png)

### Вывод:


## №7
Cоздайте любую строковую переменную и произведите над ней математическое действие умножение на любое число.

```
from for_import import say_hello

if __name__ == '__main__':
    say_hello()
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_3/ScreenKod/7.png)

### Вывод:


## №8
Посчитайте сколько раз символ "о" встречается в строке 'Hello World'.

```
from math import *

def main():
    value = int(input('Введите значение: '))
    print(sqrt(value))
    print(sin(value))
    print(cos(value))

if __name__ == '__main__':
    main()
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_3/ScreenKod/8.1.png)
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_3/ScreenKod/8.2.png)

### Вывод:


## №9
Напишите предложение Hello World' в две строки. Написанная программа должна занимать одну строку в редакторе кода.

```
from datetime import datetime as dt
from datetime import timedelta as td

def main():
    print(
        f"Сегодня {dt.today().date()}. "
        f"День недели - {dt.today().isoweekday()}"
    )
    n = int(input('Введите количество дней: '))
    today = dt.today()
    result = today + td(days=n)
    print(
        f"Через {n} дней будет {result.date()}. "
        f"День недели - {result.isoweekday()}"
    )

if __name__ == '__main__':
    main()
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_3/ScreenKod/9.png)

### Вывод:


## №10
Из предложения 'Hello World' выведите в консоль только 2 символ, а затем выведите слово
'Hello'

```
global result

def rectangle():
    a = float(input("Ширина: "))
    b = float(input("Высота: "))
    global result
    result = a * b

def triangel():
    a = float(input("Основание: "))
    h = float(input("Высота: "))
    global result
    result = 0.5 * a * h

figure = input("1-прямоугольник, 2-треугольник: ")

if figure == '1':
    rectangle()
elif figure == '2':
    triangel()

print(f"Площадь: {result}")
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_3/ScreenKod/10.png)

### Вывод:


## №11
Выведите в консоль булевую переменную False, не используя слово False в строке или изначально присвоенную булевую переменную. Программа должна занимать не более двух строк редактора кода.

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_3/ScreenKod/11(1).png)

### Вывод:


## №12
Присвоить значения трем переменным и вывести их в консоль, используя только две строки редактора кода

```
import random

def roll_dice():
  dice_value = random.randint(1, 6)
  print("Значение кубика:", dice_value)

  if dice_value in [5, 6]:
    print("Вы победили")
  elif dice_value in [3, 4]:
    print("Повторяем бросок...")
    roll_dice()
  else:
    print("Вы проиграли")


if __name__ == "__main__":
  roll_dice()
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_3/ScreenKod/12(2).png)

### Вывод:


## №13
Реализуйте ввод данных в программу, через консоль, в виде только целых чисел (тип данных int). То есть при вводе буквенных символов в консоль, программа не должна работать. Программа должна занимать не более двух строк редактора кода.

```
import datetime
import time

start_time = time.time()
while time.time() - start_time < 5:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(now)
    time.sleep(1)
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_3/ScreenKod/13(3).png)

### Вывод:


## №14
Создайте только одну строковую переменную. Длина строки должна не превышать 5 символов. На выходе мы должны получить строку длиной не менее 16 символов. Программа должна занимать не более двух строк редактора кода.

```
def avg(*args):
    return sum(args) / len(args) if args else 0

print(avg(1, 2, 3))
print(avg(4, 5, 6, 7))
print(avg())
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_3/ScreenKod/14(4.1).png)
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_3/ScreenKod/14(4.2).png)
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_3/ScreenKod/14(4.3).png)

### Вывод:


## №15
Создайте три переменные: день (тип данных - числовой), месяц (тип данных - строка), год (тип данных - числовой) и выведите в консоль текущую дату в формате: "Сегодня день месяц год. Всего хорошего!" используя F строку и оператор end внутри print), в котором вы должны написать фразу "Всего хорошего!". Программа должна занимать не более двух строк редактора кода.

```
math import sqrt

def calculate_triangle_area(a, b, c):
    s = (a + b + c) / 2
    if a + b <= c or a + c <= b or b + c <= a:
        return None
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    return area
```

```
import triangle

if __name__ == "__main__":
    try:
        a = float(input("Введите длину первой стороны треугольника: "))
        b = float(input("Введите длину второй стороны треугольника: "))
        c = float(input("Введите длину третьей стороны треугольника: "))
    except ValueError:
        print("Ошибка: Введите числовые значения для сторон треугольника.")
        exit()

    area = triangle.calculate_triangle_area(a, b, c) # triangle. - важно!

    if area is None:
        print("Треугольник с такими сторонами не существует.")
    else:
        print("Площадь треугольника:", area)
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_3/ScreenKod/15.png)

### Вывод:


