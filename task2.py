from avl_tree import root, AVLNode


def min_value(node: AVLNode) -> int | None:
    if not node:
        return None

    if not node.left:
        return node.key

    return min_value(node.left)


min_value_result = min_value(root)
print(f"Min value: {min_value_result}")
