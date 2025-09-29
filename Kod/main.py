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