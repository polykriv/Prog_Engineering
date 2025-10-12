def superset(set_1, set_2):
    if set_1 > set_2:
        print(f'Объект {set_1} является чистым супермножеством')
    elif set_1 < set_2:
        print(f'Объект {set_2} является чистым супермножеством')
    elif set_1 == set_2:
        print(f'Множества равны')
    else:
        print('Супермножества не обнаружены')

if __name__ == '__main__':
    superset({1, 4, 5, 3}, {23 ,4})
    superset({1, 4, 5, 3}, {4, 23, 4, 6})
    superset({23, 4}, {4, 23, 4, 6})
    superset({45, 454}, {23, 4})