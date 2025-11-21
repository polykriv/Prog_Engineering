def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fib_sequence = fib(200)
for i, num in enumerate(fib_sequence, 1):
    if i == 200:
        print(f"200-е число Фибоначчи: {num}")
        break