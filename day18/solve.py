class Node:
    pair: tuple

    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        if isinstance(self.val, int):
            return str(self.val)
        return f"[{str(self.left)},{str(self.right)}"


def parse_fish(number):
    root = Node()
    if isinstance(number, int):
        root.val = number
        return root

    root.left = parse_fish(number[0])
    root.right = parse_fish(number[1])
    root.left.parent = root
    root.right.parent = root

    reduce(root)
    return root


def add_to_tree(a, b):
    root = Node()
    root.left = a
    root.right = b
    root.left.parent = root
    root.right.parent = root
    reduce(root)
    return root


def reduce(node_to_reduce):
    done = True
    stack = [(node_to_reduce, 0)]
    while len(stack) > 0:

        node, depth = stack.pop()

        if node == None:
            continue

        cond = (node.left == None and node.right == None) or (node.left.val != None and node.right.val != None)
        if depth >= 4 and node.val == None and cond:
            prev_node = node.left
            cur_node = node

            while cur_node is not None and (cur_node.left == prev_node or cur_node.left is None):
                prev_node = cur_node
                cur_node = cur_node.parent

            if cur_node != None:

                cur_node = cur_node.left
                while cur_node.val == None:
                    cur_node = cur_node.right if cur_node.right is not None else cur_node.left

                cur_node.val += node.left.val

            prev_node = node.right
            cur_node = node

            while cur_node != None and (cur_node.right == prev_node or cur_node.right == None):
                prev_node = cur_node
                cur_node = cur_node.parent

            if cur_node != None:
                cur_node = cur_node.right
                while cur_node.val == None:
                    cur_node = cur_node.left if cur_node.left is not None else cur_node.right

                cur_node.val += node.right.val

            node.val = 0
            node.left = None
            node.right = None
            done = False
            break

        stack.append((node.right, depth + 1))
        stack.append((node.left, depth + 1))

    if not done:
        reduce(node_to_reduce)
        return

    stack = [node_to_reduce]
    while len(stack) > 0:
        node = stack.pop()
        if node == None:
            continue

        if node.val != None:
            if node.val >= 10:
                node.left = Node(node.val // 2)
                node.right = Node(node.val - (node.val // 2))
                node.left.parent = node
                node.right.parent = node
                node.val = None

                done = False
                break

        stack.append(node.right)
        stack.append(node.left)

    if not done:
        reduce(node_to_reduce)


def magnitude(root):
    if isinstance(root.val, int):
        return root.val

    return 3 * magnitude(root.left) + 2 * magnitude(root.right)


def get_mag(a, b):
    return magnitude((add_to_tree(a, b)))


def solve(file):
    with open(file) as inp:
        lines = inp.read().strip().split("\n")
    pairs = [eval(line) for line in lines]

    root = parse_fish(pairs[0])
    i = 1
    while i < len(pairs):
        root = add_to_tree(root, parse_fish(pairs[i]))
        i += 1

    print("p1", magnitude(root))
    max_magnitude = 0
    for ix, ip in enumerate(pairs):
        for jx, jp in enumerate(pairs):
            if ix == jx:
                continue

            a, b = parse_fish(ip), parse_fish(jp)
            max = get_mag(a, b)
            max_magnitude = max if max > max_magnitude else max_magnitude

    print("p2", max_magnitude)


if __name__ == '__main__':
    # solve("ex.txt")
    solve("in.txt")
