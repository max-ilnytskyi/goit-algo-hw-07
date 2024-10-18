from avl_tree import root, AVLNode


def max_value(node: AVLNode) -> int | None:
    if not node:
        return None

    if not node.right:
        return node.key

    return max_value(node.right)


max_value_result = max_value(root)
print(f"Max value: {max_value_result}")
