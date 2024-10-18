from avl_tree import root, AVLNode


def calc_sum(node: AVLNode) -> int | None:
    if not node:
        return None

    left_sum = calc_sum(node.left)
    right_sum = calc_sum(node.right)

    return node.key + (left_sum or 0) + (right_sum or 0)


calc_sum_result = calc_sum(root)
print(f"Sum result: {calc_sum_result}")
