class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


node_dict = {}

def copyNode(node: Node) -> Node:
    new_node = Node(node.val)
    node_dict[node] = new_node
    
    if node.neighbors:
        for neighbor in node.neighbors:
            if neighbor in node_dict:
                new_node.neighbors.append(node_dict[neighbor])
            else:
                new_node.neighbors.append(copyNode(neighbor))
        
    return new_node
    
def cloneGraph(node: Node) -> Node:
    if not node:
        return None
    
    return copyNode(node)