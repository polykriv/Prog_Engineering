class Russian:
    @staticmethod
    def greeting():
        print("Привет")

class English:
    @staticmethod
    def greeting():
        print("Hello")

    def greet(self, language):
        language.greeting()

Russian.greeting()
English.greeting()

