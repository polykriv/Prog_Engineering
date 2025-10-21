from collections import Counter

with open("input.txt", "r", encoding="utf-8") as f:
    text = f.read().lower()

words = text.split()
word_counts = Counter(words)
most_common_word, most_common_count = word_counts.most_common(1)[0]

print(f"Количество слов: {len(words)}")
print(f"Самое частое слово: '{most_common_word}' встречается {most_common_count} раз")
