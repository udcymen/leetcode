class Solution:
    def maxArea(self, height: list[int]) -> int:
        if not height or len(height) < 2:
            return 0
        
        result = 0
        start, end = 0, len(height) - 1
        
        while start < end:
            left, right = height[start], height[end]
            result = max(result, min(left, right) * (end - start))
            
            if left < right:
                start += 1
            else:
                end -= 1
                
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
    print(solution.maxArea([1,1]))
    print(solution.maxArea([4,3,2,1,4]))
    print(solution.maxArea([1,2,1]))