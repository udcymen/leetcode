class Solution:
    def canFormArray(self, arr: list[int], pieces: list[list[int]]) -> bool:
        compareArr = []
        pieceDictionary = {}
        
        for piece in pieces:
            pieceDictionary[piece[0]] = piece
            
        for num in arr:
            if num in pieceDictionary:
                compareArr.extend(pieceDictionary[num])
                
        return arr == compareArr


if __name__ == "__main__":
    solution = Solution()
    print(solution.canFormArray([85], [[85]]))
    print(solution.canFormArray([15,88], [[88],[15]]))
    print(solution.canFormArray([49,18,16], [[16,18,49]]))
    print(solution.canFormArray([91,4,64,78], [[78],[4,64],[91]]))
    print(solution.canFormArray([1,3,5,7], [[2,4,6,8]]))