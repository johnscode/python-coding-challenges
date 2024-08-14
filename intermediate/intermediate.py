from collections import Counter
import csv
import pandas as pd
import random


def list_even_squares(num):
    return [i*i for i in range(1,num+1) if i % 2 == 0]


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


class Stack:
    stack_list = []

    def push(self, x):
        self.stack_list.append(x)

    def pop(self):
        if len(self.stack_list)==0:
            return None
        return self.stack_list.pop()


class ListNode:
    data = None
    next = None
    def __init__(self, data, next):
        self.data = data
        if next is not None and type(next) != ListNode:
            raise TypeError(f"expected next to be None or another list node")
        self.next = next


class LinkedList:
    head = None

    def append(self, data):
        node = ListNode(data, None)
        if self.head is None:
            self.head = node
            return node
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = node
        return node

    def reverse(self):
        prev = None
        cur = self.head
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev

    def as_list(self):
        the_list = []
        cur = self.head
        while cur is not None:
            the_list.append(cur.data)
            cur = cur.next
        return the_list


class Hashmap:
    def __init__(self, size = 10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0]==key:
                return item[1]
        return None

    def remote(self, key):
        index = self._hash(key)
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]
                return item[1]
        return None


def process_file(filepath):
        with open(filepath,'r',newline='') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
            print(headers)
            column_index = headers.index('count')
            total = sum(float(row[column_index]) for row in reader)
            print(f"total is {total}")
            return total


def write_data(filepath):
    row_count=10
    headers = ['index','number']
    data = [[i, random.random()] for i in range(0,10)]
    with open(filepath,'w',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(data)


def process_pandas(filepath):
    df = pd.read_csv(filepath)
    total = df['count'].sum()
    print(f"total is {total}")
    return total

def upper_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@upper_decorator
def hello():
    return "hello world"
