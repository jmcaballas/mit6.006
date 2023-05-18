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
            return

        if self.right:
            self.right.insert(val)
            return

        self.right = Node(val)

    def find(self, val):
        if self.key == val:
            return val

        if val < self.key:
            return self.left.find(val) if self.left else None
        return self.right.find(val) if self.right else None


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
print(bst.find(4))
print(bst.find(1))
print(bst.find(9))
print(bst.find(8))
