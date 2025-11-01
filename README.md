# Тема_8: Введение в ООП

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
Создайте класс “Car” с атрибутами производитель и модель. Создайте объект этого класса. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями.

```
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

my_car = Car("Totota", "Corolla")
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_7/Screen/1.png)

### Вывод:
Вывод демонстрирует базовую операцию создания файла с несколькими строками и хранение его в директории с программой. Это первая ступень работы с файлами, закрепляет понимание физического расположения и создания текстовых файлов.

## №2
Дополните код из первого задания, добавив в него атрибуты и методы класса, заставьте машину “поехать”. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"Driving the {self.make} {self.model}")


my_car = Car("Totota", "Corolla")
my_car.drive()
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_7/Screen/2.png)

### Вывод:
Пример показывает, как открыть файл в режиме чтения, считать только первую строку и закрыть файл вручную. Это базовый способ работы с файлами, требующий аккуратного закрытия ресурсов после использования.

## №3
Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте констСоздайте новый класс “ElectricCar” с методом “charge” и атрибутом емкость батареи. Реализуйте его наследование от класса, созданного в первом задании. Заставьте машину поехать, а потом заряжаться. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```
fclass Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"Driving the {self.make} {self.model}")

class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")

my_electric_car = ElectricCar("Tesla", "Model S", 75)
my_electric_car.drive()
my_electric_car.charge()
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_7/Screen/3.png)

### Вывод:
Демонстрируется чтение всех строк из файла в виде списка строк с помощью open()/close(). Позволяет удобно получить весь текстовый контент файла в память для последующей обработки.

## №4
Реализуйте инкапсуляцию для класса, созданного в первом задании. Создайте защищенный атрибут производителя и приватный атрибут модели. Вызовите защищенный атрибут и заставьте машину поехать. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```
class Car:
    def __init__(self, make, model):
        self._make = make
        self.__model = model

    def drive(self):
        print(f"Driving the {self._make} {self.__model}")

my_car = Car("Totota", "Corolla")
print(my_car._make)
my_car.drive()
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_7/Screen/4.png)

### Вывод:
Показывается более безопасный и удобный способ чтения файла с помощью конструкции with open(), которая автоматически закрывает файл после окончания блока. Это предпочтительная практика при работе с файлами.

## №5
Реализуйте полиморфизм создав основной (общий) класс “Shape”, а также еще два класса “Rectangle” и “Circle”. Внутри последних двух классов реализуйте методы для подсчета площади фигуры. После этого создайте массив с фигурами, поместите туда круг и прямоугольник, затем при помощи цикла выведите их площади. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

rect = Rectangle(4, 5)
print(rect.area())

circle = Circle(3)
print(circle.area())
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_7/Screen/5.png)

### Вывод:
Пример итерации по файлу в цикле, где каждая строка выводится отдельно. Демонстрирует эффективный способ последовательного чтения больших файлов без загрузки всего содержимого в память.


#Самостоятельная работа по Python

## №6
Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print(f"Book: '{self.title}' by {self.author}")

my_book = Book("1984", "George Orwell")
my_book.display()

```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_7/Screen/11(1)%D0%A1%D1%82%D0%B0%D1%82%D1%8C%D1%8F.png)
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_7/Screen/11(1).png)

### Вывод:
Выполнено подсчёт слов в текстовом файле и определение самого часто встречающегося слова. Выводит статистику, полезную для анализа больших текстов в различных приложениях.

## №7
Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display(self):
        print(f"Book: '{self.title}' by {self.author}, {self.pages} pages")

    def is_long(self):
        return self.pages > 300

my_book = Book("1984", "George Orwell", 328)
my_book.display()
print("Is long book:", my_book.is_long())

```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_7/Screen/12(2).png)
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_7/Screen/12(2)%D1%83%D1%87%D0%B5%D1%82%20%D1%80%D0%B0%D1%81%D1%85%D0%BE%D0%B4%D0%BE%D0%B2.png)

### Вывод:
Разработана программа учёта расходов с возможностью ввода через консоль, сохранения в JSON файл и просмотра данных. Это пример полноценного консольного приложения с работой с файлами и сериализацией данных.

## №8
Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display(self):
        print(f"Book: '{self.title}' by {self.author}, {self.pages} pages")

class EBook(Book):
    def __init__(self, title, author, pages, filesize):
        super().__init__(title, author, pages)
        self.filesize = filesize

    def display(self):
        super().display()
        print(f"File size: {self.filesize} MB")

my_ebook = EBook("1984", "George Orwell", 328, 2)
my_ebook.display()

```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_7/Screen/13(3).png)

### Вывод:
Программа считывает текст файла и выводит статистику по количеству букв латинского алфавита, слов и строк, что полезно для анализа текстовых данных и подготовке отчётов.

## №9
Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display(self):
        print(f"Book: '{self.title}' by {self.author}, {self.pages} pages")

class EBook(Book):
    def __init__(self, title, author, pages, filesize):
        super().__init__(title, author, pages)
        self.__filesize = filesize  # приватный атрибут с двойным подчёркиванием

    def display(self):
        print(f"Book: '{self.title}' by {self.author}, {self.pages} pages")
        print(f"File size: {self.__filesize} MB")

    def get_filesize(self):
        return self.__filesize

    def set_filesize(self, size):
        if size > 0:
            self.__filesize = size
        else:
            print("File size must be positive")

my_ebook = EBook("1984", "George Orwell", 328, 2)
my_ebook.display()
print("Current filesize:", my_ebook.get_filesize())
my_ebook.set_filesize(3)
print("Updated filesize:", my_ebook.get_filesize())
```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_7/Screen/14(4).png)

### Вывод:
Реализовано цензурирование текста с заменой запрещённых слов на символы *. Учебная задача по обработке текста, регулярным выражениям, работам с файлами и регистро-независимому поиску.

## №10
Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display(self):
        print(f"Book: '{self.title}' by {self.author}, {self.pages} pages")

class AudioBook(Book):
    def __init__(self, title, author, length):
        super().__init__(title, author, pages=0)  # страниц нет
        self.length = length  # длительность в минутах

    def display(self):
        print(f"Audiobook: '{self.title}' by {self.author}, length {self.length} minutes")

def show_info(book):
    book.display()

book1 = Book("1984", "George Orwell", 328)
audiobook = AudioBook("1984", "George Orwell", 660)

show_info(book1)
show_info(audiobook)

```

### Результат
![Меню](https://github.com/polykriv/Prog_Engineering/blob/Tema_7/Screen/15(5).png)

### Вывод:
Задача научила подсчитывать частоту вхождения заданной буквы в файл, используя коллекции. Полезное упражнение для анализа текста на уровне символов и взаимодействия с файлами.


### Вывод:
Научились работать с уникальными элементами через множества и проверять размеры коллекций.
