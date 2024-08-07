
def is_even(num):
    return num & 1 == 0

def sum_list(list):
    sum=0
    for a in list:
        sum += a
    return sum

def reverse_string(word):
    if not isinstance(word, str):
        raise TypeError("Input must be a string")
    return word[::-1]

