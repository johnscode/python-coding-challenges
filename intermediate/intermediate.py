

def binary_search(key, alist):
    n = len(alist) >> 1
    item = alist[n]
    if item==key:
        return n
    if n==0:
        return -1
    if item>key:
        return binary_search(key, alist[0:n:1])
    else:
        res = binary_search(key, alist[n::1])
        if res<0:
            return res
        return n+res

def remove_duplicates(alist):
    seen = set()
    result = []
    for item in alist:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

