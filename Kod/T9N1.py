class Polina:
    __slots__ = ['name']

    def __init__(self, name):
        if name == 'Полина':
            self.name = f"Да, я {name}"
        else:
            self.name = f"Я не {name}, а Полина"

person1 = Polina('Дарья')
person2 = Polina('Полина')
print(person1.name)
print(person2.name)