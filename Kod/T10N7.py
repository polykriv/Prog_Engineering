class EmptyFileError(Exception):
    pass


def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read().strip()
            if not content:
                raise EmptyFileError("файл пустой")
            print(f"Содержимое файла: {content}")
    except FileNotFoundError:
        print("Файл не найден")
    except EmptyFileError as e:
        print(e)


# Тестирование
if __name__ == '__main__':
    # Создаем пустой файл и файл с данными для теста
    with open('empty.txt', 'w') as f:
        pass

    with open('data.txt', 'w') as f:
        f.write("Пример данных из файла")

    read_file('empty.txt')  # Вызовет исключение
    read_file('data.txt')  # Выведет содержимое