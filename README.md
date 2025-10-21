# Тема_7: Работа с файлами (ввод, вывод)

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
| Задание 10| + |   |

#Лабораторная работа по Python
## №1
Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк.

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_7/Screen/1.png)

### Вывод:
Вывод демонстрирует базовую операцию создания файла с несколькими строками и хранение его в директории с программой. Это первая ступень работы с файлами, закрепляет понимание физического расположения и создания текстовых файлов.

## №2
Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().

```
f = open('input.txt', 'r')
print(f.readline())
f.close()
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_7/Screen/2.png)

### Вывод:
Пример показывает, как открыть файл в режиме чтения, считать только первую строку и закрыть файл вручную. Это базовый способ работы с файлами, требующий аккуратного закрытия ресурсов после использования.

## №3
Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open()/close().

```
f = open('input.txt', 'r')
print(f.readlines())
f.close()
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_7/Screen/3.png)

### Вывод:
Демонстрируется чтение всех строк из файла в виде списка строк с помощью open()/close(). Позволяет удобно получить весь текстовый контент файла в память для последующей обработки.

## №4
Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().

```
with open('input.txt') as f:
    print((f.readlines()))
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_7/Screen/4.png)

### Вывод:
Показывается более безопасный и удобный способ чтения файла с помощью конструкции with open(), которая автоматически закрывает файл после окончания блока. Это предпочтительная практика при работе с файлами.

## №5
Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().

```
with open('input.txt') as f:
    for line in f:
        print(line)
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_7/Screen/5.png)

### Вывод:
Пример итерации по файлу в цикле, где каждая строка выводится отдельно. Демонстрирует эффективный способ последовательного чтения больших файлов без загрузки всего содержимого в память.

## №6
Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.

```  python
with open('input.txt', 'a+') as f:
    f.write('\nNew line')

with open ('input.txt', 'r') as f:
    result = f.readlines()
    print(result)
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_7/Screen/6.png)

### Вывод:
Код и вывод демонстрируют возможность добавления новой строки в существующий файл с помощью режима 'a+' и последующего чтения обновленного содержимого. Это полезно для ведения логов или накопления данных без перезаписи.

## №7
Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Также не забудьте проверить что изменения сохранилась в файле.

```
lines = ['one', 'two', 'three']
with open('input.txt', 'w') as f:
    for line in lines:
        f.write('\nLa La La ' + line)
    print('Done!')
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_7/Screen/7.png)
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_7/Screen/7%D0%B8%D1%82%D0%BE%D0%B3.png)

### Вывод:
Показывает, как полностью перезаписать содержимое файла данными из списка, используя режим 'w'. Помогает понять принципы перезаписи и форматирования данных при сохранении в файл.

## №8
Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).

```
import os

def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит:')
    print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
    print(f'Файлы: {", ".join([file for file in catalog[2]])}')
    print('-' * 40)

print_docs('D:\For PI')
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_7/Screen/8.png)

### Вывод:
Функция и результат показывают рекурсивный обход заданной директории и вывод содержимого всех вложенных папок и файлов. Это важно для администрирования и анализа структуры каталогов.

## №9
Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько). Проверьте работоспособность программы на своем наборе данных

```
def longest_words(file):
    with open(file, encoding='utf-8') as f:
        words = f.read().split()
        max_length = len(max(words, key=len))
        for word in words:
            if len(word) == max_length:
                sought_words = word

        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words

print(longest_words('input.txt'))
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_7/Screen/9.png)

### Вывод:
Задача с поиском и выводом слова максимальной длины из файла учит работе с текстом, разбивке на слова, нахождению максимальных значений и условий для вывода.

## №10
Требуется создать csv-файл «rows_300.csv» со следующими столбцами:
№ - номер по порядку (от 1 до 300);
Секунда – текущая секунда на вашем ПК;
Микросекунда – текущая миллисекунда на часах.
Для наглядности на каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.

```
import csv
import time
from datetime import datetime

with open('rows_300.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['№', 'Секунда', 'Микросекунда'])

    for i in range(1, 301):
        now = datetime.now()
        sec = now.second
        microsec = int(now.microsecond / 1000)
        writer.writerow([i, sec, microsec])
        time.sleep(0.01)
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_7/Screen/10.png)
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_7/Screen/10%D0%B8%D1%82%D0%BE%D0%B3.png)

### Вывод:
Пример демонстрирует создание CSV-файла с использованием встроенного модуля csv, с записью нумерации, текущего времени (секунд и миллисекунд), и искусственной задержкой для иллюстрации динамики работы.

#Самостоятельная работа по Python

## №11
Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.

```
from collections import Counter

with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read().lower()

words = text.split()
word_counts = Counter(words)
most_common_word, most_common_count = word_counts.most_common(1)[0]

print(f"Количество слов: {len(words)}")
print(f"Самое частое слово: '{most_common_word}' встречается {most_common_count} раз")

```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_7/Screen/11(1)%D0%A1%D1%82%D0%B0%D1%82%D1%8C%D1%8F.png)
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_7/Screen/11(1).png)

### Вывод:
Выполнено подсчёт слов в текстовом файле и определение самого часто встречающегося слова. Выводит статистику, полезную для анализа больших текстов в различных приложениях.

## №12
У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.

```
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
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_7/Screen/12(2).png)
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_7/Screen/12(2)%D1%83%D1%87%D0%B5%D1%82%20%D1%80%D0%B0%D1%81%D1%85%D0%BE%D0%B4%D0%BE%D0%B2.png)

### Вывод:
Разработана программа учёта расходов с возможностью ввода через консоль, сохранения в JSON файл и просмотра данных. Это пример полноценного консольного приложения с работой с файлами и сериализацией данных.

## №13
Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк.

Текст в файле:
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.

Ожидаемый результат:
Input file contains:
108 letters
20 words
4 lines

```
with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

text = "".join(lines)
# Фильтруем буквы латинского алфавита
letters = [c for c in text if c.isalpha() and c.isascii()]
words = text.split()
num_lines = len(lines)

print(f"Файл содержит:\n{len(letters)} букв\n{len(words)} слов\n{num_lines} строк")
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_7/Screen/13(3).png)

### Вывод:
Программа считывает текст файла и выводит статистику по количеству букв латинского алфавита, слов и строк, что полезно для анализа текстовых данных и подготовке отчётов.

## №14
Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****.

Запрещенные слова:
hello email python the exam wor is

Предложение для проверки:
Hello, world! Python IS the programming language of thE future. My
EMAIL is....
PYTHON is awesome!!!!

Ожидаемый результат:
*****, *** ** ** *** programming language of *** future. My
***** **....
****** ** awesome!!!!

```
import re

# Загрузка запрещённых слов из файла input.txt
with open("input.txt", "r", encoding="utf-8") as f:
    banned_words = f.read().lower().split()

def censor_text(text, banned):
    def replacer(match):
        return "*" * len(match.group())
    pattern = re.compile("|".join(map(re.escape, banned)), re.IGNORECASE)
    return pattern.sub(replacer, text)

sentence = "Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!"
print(censor_text(sentence, banned_words))
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_7/Screen/14(4).png)

### Вывод:
Реализовано цензурирование текста с заменой запрещённых слов на символы *. Учебная задача по обработке текста, регулярным выражениям, работам с файлами и регистро-независимому поиску.

## №15
Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.

```
from collections import Counter

with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read().lower()

# Подсчитываем все буквы латинского алфавита
letters = [c for c in text if c.isalpha() and c.isascii()]
counter = Counter(letters)

letter = input("Введите букву для подсчёта её частоты: ").lower()

# Выводим количество вхождений этой буквы, если есть
count = counter.get(letter, 0)
print(f"Буква '{letter}' встречается {count} раз(а).")
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_7/Screen/15(5).png)

### Вывод:
Задача научила подсчитывать частоту вхождения заданной буквы в файл, используя коллекции. Полезное упражнение для анализа текста на уровне символов и взаимодействия с файлами.


### Вывод:
Научились работать с уникальными элементами через множества и проверять размеры коллекций.
