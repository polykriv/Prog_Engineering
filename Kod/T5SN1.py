def analyze_restaurant_visits(visits):

    num_checks = len(visits)
    unique_visitors = len(set(visits))

    visitor_counts = {}
    for visitor in visits:
        if visitor in visitor_counts:
            visitor_counts[visitor] += 1
        else:
            visitor_counts[visitor] = 1

    most_frequent_visitor = None
    max_visits = 0
    for visitor, count in visitor_counts.items():
        if count > max_visits:
            most_frequent_visitor = visitor
            max_visits = count

    print("--- Статистика посещений ресторана ---")
    print(f"Всего выдано чеков: {num_checks}")
    print(f"Количество уникальных посетителей: {unique_visitors}")
    if most_frequent_visitor:
        print(f"Работник, посетивший ресторан больше всех раз: {most_frequent_visitor} (посещений: {max_visits})")
    else:
        print("Посещений не было.")

# Данные о посещениях ресторана (пример)
restaurant_visits = [8734, 2345, 8201, 6621, 9999, 1234, 5678, 8201, 8888, 4321, 3365,
                    1478, 9865, 5555, 7777, 9998, 1111, 2222, 3333, 4444, 5656, 6666,
                    5410, 7778, 8889, 4445, 1439, 9604, 8201, 3365, 7502, 3016, 4928,
                    5837, 8201, 2643, 5017, 9682, 8530, 3250, 7193, 9051, 4506, 1987,
                    3365, 5410, 7168, 7777, 9865, 5678, 8201, 4445, 3016, 4506, 4506]

analyze_restaurant_visits(restaurant_visits)