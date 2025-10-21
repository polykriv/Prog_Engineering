with open("input.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

text = "".join(lines)
# Фильтруем буквы латинского алфавита
letters = [c for c in text if c.isalpha() and c.isascii()]
words = text.split()
num_lines = len(lines)

print(f"Файл содержит:\n{len(letters)} букв\n{len(words)} слов\n{num_lines} строк")

