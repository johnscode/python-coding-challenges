import collections

def check_for_anagram(s1, s2):
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())


class LRUCache(collections.OrderedDict):
    def __init__(self, sixe):
        self.capacity = sixe

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.move_to_end(key)
        if len(self)>self.capacity:
            self.popitem(last=False)

    def get(self, key):
        value = super().get(key)
        self.move_to_end(key)
        return value



