import math

def calculate_triangle_area(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return None

    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


def analyze_triangle_sides(list1, list2, list3):
    max_sides = [max(list1), max(list2), max(list3)]
    min_sides = [min(list1), min(list2), min(list3)]

    area_max = calculate_triangle_area(max_sides[0], max_sides[1], max_sides[2])
    area_min = calculate_triangle_area(min_sides[0], min_sides[1], min_sides[2])

    print("Площади треугольников")
    if area_max:
        print(f"Площадь треугольника из максимальных сторон: {area_max:.2f}")
    else:
        print("Треугольник из максимальных сторон не существует.")

    if area_min:
        print(f"Площадь треугольника из минимальных сторон: {area_min:.2f}")
    else:
        print("Треугольник из минимальных сторон не существует.")


# Данные о сторонах треугольников
one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

analyze_triangle_sides(one, two, three)
