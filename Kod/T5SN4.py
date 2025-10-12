def fix_grades(grades):

    new_grades = [4 if grade == 3 else grade for grade in grades if grade != 2]
    return new_grades

grades1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
grades2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
grades3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]

print("Исправление оценок Борисом")
print(f"Оценки до: {grades1}, После: {fix_grades(grades1)}")
print(f"Оценки до: {grades2}, После: {fix_grades(grades2)}")
print(f"Оценки до: {grades3}, После: {fix_grades(grades3)}")