

def factorial(n):
    if not isinstance(n, int):
        raise TypeError("expected integer")

    if n < 0:
        raise ValueError("expected positive int")

    if n == 0 or n == 1:
        return 1

    fact = 1
    for i in range(2, n+1):
        fact *= i
    return fact

def fibonacci(n):
    if not isinstance(n, int):
        raise TypeError("expected integer")

    if n < 2:
        raise ValueError("expected positive int > 0")

    fib = [1, 1]
    for i in range(2, n+1):
        fib.append(fib[i-2]+fib[i-1])

    print(f'n: {n} - {fib}')
    return fib

def palindrome_check(word):
    trimmed = ''.join(char.lower() for char in word if char.isalnum())
    return trimmed == trimmed[::-1]

