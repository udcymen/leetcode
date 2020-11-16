class Solution:
    def longestMountain(self, A: list[int]) -> int:
        if not A or len(A) == 0:
            return 0
        
        start, result = 0, 0
        N = len(A)
        
        while start < N:
            curr = start
            
            if curr + 1 < N and A[curr] < A[curr + 1]:
                while curr + 1 < N and A[curr] < A[curr + 1]:
                    curr += 1
                    
                if curr + 1 < N and A[curr] > A[curr + 1]:
                    curr += 1
                    
                    while curr + 1 < N and A[curr] > A[curr + 1]:
                        curr += 1

                    result = max(result, curr - start + 1)
                    
            start = max(start + 1, curr)
        
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestMountain([2,1,4,7,3,2,5]))
    print(solution.longestMountain([2,3]))
    print(solution.longestMountain([2,2,2]))