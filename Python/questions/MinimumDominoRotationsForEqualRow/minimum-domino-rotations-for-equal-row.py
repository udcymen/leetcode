def rotate(num: int, l: int, A: list[int], B: list[int]) -> int:
    rotate_a, rotate_b = 0, 0

    for i in range(l):
        a, b = A[i], B[i]

        if num != a and num != b:
            return -1
        elif num != a:
            rotate_a += 1
        elif num != b:
            rotate_b += 1

    return min(rotate_a, rotate_b)

def minDominoRotations(A: list[int], B: list[int]) -> int:
    if not A or not B:
        return -1

    l = min(len(A), len(B))
    result = rotate(A[0], l, A, B)

    if result != -1:
        return result
    else:
        return rotate(B[0], l, A, B)


if __name__ == "__main__":
    print(minDominoRotations([2,1,2,4,2,2], [5,2,6,2,3,2]))
    print(minDominoRotations([3,5,1,2,3], [3,6,3,3,4]))
    print(minDominoRotations([1,2,1,1,1,2,2,2], [2,1,2,2,2,2,2,2]))
    


