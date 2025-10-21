import re

# Загрузка запрещённых слов из файла input.txt
with open("input.txt", "r", encoding="utf-8") as f:
    banned_words = f.read().lower().split()

def censor_text(text, banned):
    def replacer(match):
        return "*" * len(match.group())
    pattern = re.compile("|".join(map(re.escape, banned)), re.IGNORECASE)
    return pattern.sub(replacer, text)

sentence = "Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!"
print(censor_text(sentence, banned_words))