def fibonacci_first_n(n):
    fib = []
    a, b = 0, 1

    for _ in range(n):
        fib.append(a)
        a, b = b, a + b

    return fib
n = int(input("Enter n: "))
print(fibonacci_first_n(n))