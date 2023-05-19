from binary_search_tree import Node


def get_height(node):
    # height = length (# edges) of longest downward path to a leaf
    if not node:
        return -1
    if node.left or node.right:
        return 1 + max(get_height(node.left), get_height(node.right))
    else:
        return 0


def test_invariant(node):
    return abs(get_height(node.left) - get_height(node.right)) <= 1


def rotate_left(node):
    new_root = node.right
    node.right = new_root.left
    new_root.left = node

    return new_root


def rotate_right(node):
    new_root = node.left
    node.left = new_root.right
    new_root.right = node

    return new_root


def balance(node):
    if not node:
        return None

    balance(node.left)
    balance(node.right)

    if test_invariant(node):
        return

    if get_height(node.left) > get_height(node.right):
        return rotate_right(node.left)
    else:
        return rotate_left(node.right)


def insert(root, val):
    if not root:
        return Node(val)

    if val < root.key:
        root.left = insert(root.left, val)
    elif val > root.key:
        root.right = insert(root.right, val)

    return balance(root)


def test_balance():
    values = [5, 4, 3, 2, 1]

    test_node = Node(None)
    for value in values:
        test_node.insert(value)

    print("AVL invariant before balancing:", test_invariant(test_node))
    balance(test_node)
    print("AVL invariant after balancing:", test_invariant(test_node))


def test_insert():
    avl_tree = Node(None)

    values = [5, 3, 7, 2, 4, 6, 8]
    for value in values:
        avl_tree.insert(value)

    is_balanced = test_invariant(avl_tree)
    avl_tree.print_tree()
    print("Is the AVL tree balanced?", is_balanced)


print("Test Balance:")
test_balance()
print("Test Insert:")
test_insert()
