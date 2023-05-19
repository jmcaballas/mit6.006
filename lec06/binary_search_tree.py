class Node:
    def __init__(self, key=None):
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
