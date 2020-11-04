def findMinHeightTrees(n: int, edges: list[list[int]]) -> list[int]:
    neighbours, degrees = {}, {}
    
    for i in range(n):
        neighbours[i] = []
        degrees[i] = 0
    
    for a, b in edges:
        neighbours[a].append(b)
        neighbours[b].append(a)
        degrees[a] += 1
        degrees[b] += 1
        
    result = set([i for i in range(n)])
    
    while len(result) > 2:
        leaves = [node for node in result if degrees[node] == 1]
        
        for leaf in leaves:
            for neighbour in neighbours[leaf]:
                if degrees[neighbour] > 1:
                    degrees[neighbour] -= 1
            result.remove(leaf)
        
    return list(result)


if __name__ == "__main__":
    print(findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))
    print(findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))
    print(findMinHeightTrees(1, []))
    print(findMinHeightTrees(2, [[1,0]]))