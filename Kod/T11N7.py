def fib(n):
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

with open('fib.txt', 'w') as f:
    for i, num in enumerate(fib(200), 1):
        f.write(f"{num}\n")
        if i == 200:
            print(f"200-е число Фибоначчи: {num}")