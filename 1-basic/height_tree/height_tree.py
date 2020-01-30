# Определить высоту дерева

def height_for_node(lst, node):
    height = 0
    while node != -1:
        node = lst[node]
        height += 1
    return height


def height_tree(tree):
    lst = list(map(int, tree.split()))
    max_height = 0
    for node in range(len(lst)):
        max_height = max(max_height, height_for_node(lst, node))
    return max_height


if __name__ == '__main__':
    n = int(input())
    tree = input()
    print(height_tree(tree))
