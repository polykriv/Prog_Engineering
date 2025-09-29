from math import sqrt

def calculate_triangle_area(a, b, c):
    s = (a + b + c) / 2
    if a + b <= c or a + c <= b or b + c <= a:
        return None
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    return area