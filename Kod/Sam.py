class Tomato:
    states = {
        0: 'отсутствует',
        1: 'цветение',
        2: 'зеленый',
        3: 'красный'
    }

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 3:
            self._state += 1
        print(f'Томат {self._index} теперь на стадии: {Tomato.states[self._state]}')

    def is_ripe(self):
        return self._state == 3


class TomatoBush:
    def __init__(self, num_tomatoes):
        self.tomatoes = [Tomato(i) for i in range(num_tomatoes)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        self.tomatoes = []


class Gardener:
    @staticmethod
    def knowledge_base():
        print("""
        СПРАВКА ПО САДОВОДСТВУ:
        - Томаты проходят 4 стадии созревания: отсутствует, цветение, зеленый, красный
        - Садовник должен ухаживать за растением, пока все томаты не созреют
        - Собирать урожай можно только когда все томаты красные
        """)

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print(f"{self.name} ухаживает за растением...")
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            print(f"{self.name} собирает урожай! Все томаты созрели.")
            self._plant.give_away_all()
            return True
        else:
            print(f"Предупреждение: томаты еще не дозрели! {self.name} должен продолжать ухаживать.")
            return False


if __name__ == "__main__":
    # 1 тест
    print("=== ТЕСТ 1: Вызов справки по садоводству ===")
    Gardener.knowledge_base()

    # 2 тест
    print("\n=== ТЕСТ 2: Создание объектов ===")
    bush = TomatoBush(3)  # куст с 3 томатами
    gardener = Gardener("Иван", bush)
    print(f"Создан садовник: {gardener.name}")
    print(f"Создан куст с {len(bush.tomatoes)} томатами")

    # 3 тест
    print("\n=== ТЕСТ 3: Уход за растениями ===")
    gardener.work()

    # 4 тест
    print("\n=== ТЕСТ 4: Попытка сбора незрелого урожая ===")
    gardener.harvest()

    # Продолжаем ухаживать за ними
    print("\n=== ТЕСТ 5: Продолжение ухода ===")
    for i in range(3):  # нужно еще 3 цикла ухода для полного созревания
        print(f"\n--- Цикл ухода {i + 1} ---")
        gardener.work()
        if gardener.harvest():  # если урожай собран
            break

    # 5 тест
    if bush.tomatoes:
        print("\n=== ТЕСТ 6: Финальный сбор урожая ===")
        gardener.harvest()

    print("\n=== ПРОГРАММА ЗАВЕРШЕНА ===")