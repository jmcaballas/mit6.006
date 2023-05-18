class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

    def print_tree(self):
        if self.left:
            self.left.print_tree()

        if self.key is not None:
            print(self.key, end=" ")

        if self.right:
            self.right.print_tree()

    def insert(self, val):
        if not self.key:
            self.key = val
            return

        if self.key == val:
            return

        if val < self.key:
            if self.left:
                self.left.insert(val)
                return

            self.left = Node(val)
            self.left.parent = self
            return

        if self.right:
            self.right.insert(val)
            return

        self.right = Node(val)
        self.right.parent = self

    def find(self, val):
        if self.key == val:
            return self

        if val < self.key:
            return self.left.find(val) if self.left else None
        return self.right.find(val) if self.right else None

    def find_min(self):
        return self.key if not self.left else self.left.find_min()

    def next_larger(self):
        if self.right:
            node = self.right
            while node.left:
                node = node.left
            return node

        node = self
        while node.parent:
            if node == node.parent.right:
                node = node.parent
            else:
                return node.parent
        return None


bst = Node(None)
bst.insert(5)
bst.insert(2)
bst.insert(7)
bst.insert(1)
bst.insert(3)
bst.insert(6)
bst.insert(8)
bst.print_tree()

print("")
print(bst.find(4).key if bst.find(4) else None)
print(bst.find(1).key)
print(bst.find(9).key if bst.find(4) else None)
print(bst.find(8).key)
print(bst.find_min())
print(bst.find(3).next_larger().key)
print(bst.find(8).next_larger().key if bst.find(8).next_larger() else None)
