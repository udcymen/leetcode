class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals or len(intervals) <= 1:
            return intervals
        
        intervals.sort()
        
        index = 1
        curr = intervals[0]
        result = []
        
        while index < len(intervals):
            while index < len(intervals) and intervals[index][0] <= curr[1]:
                curr[1] = max(curr[1], intervals[index][1])
                index += 1
            
            result.append(curr)
            
            if index < len(intervals):
                curr = intervals[index]
                
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.merge([[1,3],[2,6],[8,10],[15,18]]))
    print(solution.merge([[1,4],[4,5]]))