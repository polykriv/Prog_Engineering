from collections import Counter

with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.read().lower()

# Подсчитываем все буквы латинского алфавита
letters = [c for c in text if c.isalpha() and c.isascii()]
counter = Counter(letters)

letter = input("Введите букву для подсчёта её частоты: ").lower()

# Выводим количество вхождений этой буквы, если есть
count = counter.get(letter, 0)
print(f"Буква '{letter}' встречается {count} раз(а).")
