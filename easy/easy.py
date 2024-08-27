
def compare_versions(version1: str, version2: str):
    # split version strings into list of numberrs
    v1 = [int(v) for v in version1.split('.')]
    v2 = [int(v) for v in version2.split('.')]

    print(f"v1: {v1}")
    print(f"v2: {v2}")
    # pad shortest version
    maxlen = max(len(v1), len(v2))
    print(f"max len {maxlen}")
    v1 += [0] *(maxlen-len(v1))
    v1 += [0] *(maxlen-len(v2))
    print(f"update v1: {v1}")
    print(f"updated v2: {v2}")
    for i in range(maxlen):
        if v1[i]<v2[i]:
            return -1
        elif v1[i]>v2[i]:
            return 1
    return 0

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

    if n<0:
        raise ValueError("expected integer > 0")

    if n == 0:
        return [0]
    if n == 1:
        return [0]

    fib = [0, 1]
    for i in range(2, n+1):
        fib.append(fib[i-2]+fib[i-1])

    print(f'n: {n} - {fib}')
    return fib


def fib2(num):
    fib = [0,1]
    for n in range(2, num+1):
        fib.append(fib[n-2]+fib[n-1])
    return fib


# def palindrome_check(word):
#     trimmed = ''.join(char.lower() for char in word if char.isalnum())
#     return trimmed == trimmed[::-1]


def palindrome_check(str):
    lower = str.lower()
    trimmed = lower.strip()
    return trimmed == trimmed[::-1]

