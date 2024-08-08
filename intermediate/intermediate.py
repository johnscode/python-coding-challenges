from collections import Counter

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

def most_frequent(alist):
   c = Counter(alist)
   counts = c.most_common(1)
   return counts[0][0]

# def most_frequent(alist):
#     adict = {}
#     for item in alist:
#         if adict.get(item) is None:
#             adict[item]=1
#         else:
#             adict[item]=adict[item]+1
#     max=0
#     max_key=None
#     for k,v in adict.items():
#         if v>max:
#             max_key=k
#     return adict[max_key]