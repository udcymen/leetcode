def minCostToMoveChips(position: list[int]) -> int:
    odd = 0
    even = 0
    
    for value in position:
        if value % 2 == 0:
            even += 1
        else:
            odd += 1

    return min(odd, even)


if __name__ == "__main__":
    print(minCostToMoveChips([1,2,3]))
    print(minCostToMoveChips([2,2,2,3,3]))
    print(minCostToMoveChips([1,1000000000]))
    print(minCostToMoveChips([1,2,2,2,2,2]))