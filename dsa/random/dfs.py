class Node:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.children = []

def dfs(node):
    """
    Performs a depth-first search to calculate the sum of values
    for each subtree rooted at 'node'. Returns the tuple:
    (subtree_sum, max_subtree_sum, node_with_max_sum)
    """
    subtree_sum = node.value
    max_sum = float('-inf')
    max_node = None

    for child in node.children:
        child_sum, child_node = dfs(child)
        subtree_sum += child_sum

        if child_sum > max_sum:
            max_sum = child_sum
            max_node = child_node

    if subtree_sum > max_sum:
        max_sum = subtree_sum
        max_node = node

    return subtree_sum, max_node

def find_max_node(root):
    """
    Find the node with the maximum subtree sum and the sum.
    Returns (node_name, max_sum)
    """
    max_sum, max_node = dfs(root)
    return max_node.name, max_sum

if __name__ == "__main__":
    # Create the specific company structure as given in the question

    # CEO node
    ceo = Node("ceo", 300000)

    # Manager nodes
    manager1 = Node("manager1", 20000)
    manager2 = Node("manager2", 170000)

    # Employee nodes under manager2
    employee1 = Node("employee1", 20000)
    employee2 = Node("employee2", 30000)

    # Build the tree structure
    ceo.children.extend([manager1, manager2])
    manager2.children.extend([employee1, employee2])

    node_name, max_sum = find_max_node(ceo)
    print(f"Node with max subtree sum: {node_name}, Sum: {max_sum}")