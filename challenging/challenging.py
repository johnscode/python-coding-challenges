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


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self.recurse_insert(self.root, data)

    def recurse_insert(self, current, data):
        if data < current.data:
            if current.left is None:
                current.left = TreeNode(data)
            else:
                self.recurse_insert(current.left, data)
        elif data > current.data:
            if current.right is None:
                current.right = TreeNode(data)
            else:
                self.recurse_insert(current.right, data)

    def inorder(self):
        self.recurse_inorder(self.root)

    def recurse_inorder(self, current):
        if current is not None:
            self.recurse_inorder(current.left)
            print(f"{current.data} ")
            self.recurse_inorder(current.right)

    def preorder(self):
        self.recurse_preorder(self.root)

    def recurse_preorder(self, current):
        if current is not None:
            print(f"{current.data} ")
            self.recurse_preorder(current.left)
            self.recurse_preorder(current.right)

    def postorder(self):
        self.recurse_postorder(self.root)

    def recurse_postorder(self, current):
        if current is not None:
            self.recurse_postorder(current.left)
            self.recurse_postorder(current.right)
            print(f"{current.data} ")

    def level_order(self):
        queue = []
        self._queue_insert(queue, self.root)
        while len(queue)>0:
            current = queue.pop(0)
            self._queue_insert(queue, current.left)
            self._queue_insert(queue, current.right)
            print(f"{current.data} ")

    def _queue_insert(self, queue, node):
        if node is not None:
            queue.append(node)

class TrieNode:
    def __init__(self):
        self.kids = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for c in word:
            if c not in current.kids:
                current.kids[c] = TrieNode()
            current = current.kids[c]
        current.isEnd = True

    def search(self, word):
        current = self.root
        for c in word:
            if c not in current.kids:
                return False
            current = current.kids[c]
        return current.isEnd

    def find_completions(self, node, prefix="", words=None):
        if words is None:
            words = []
        if node.isEnd:
            words.append(prefix)
        if len(words) == 5:
            return words
        for c, kid in node.kids.items():
            words = self.find_completions(kid, prefix+c,words)
            if len(words) == 5:
                return words
        return words




