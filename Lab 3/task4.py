def fibunaci(n):
    fib_sequence = []
    a = 0
    b = 1
    for _ in range(n + 1):
        if a > n:
            break
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

x = int(input("Enter a num: "))
print(fibunaci(x))