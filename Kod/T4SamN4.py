def avg(*args):
    return sum(args) / len(args) if args else 0

print(avg(1, 2, 3))
print(avg(4, 5, 6, 7))
print(avg())