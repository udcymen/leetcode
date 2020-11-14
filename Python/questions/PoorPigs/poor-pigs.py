class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        totolTest = minutesToTest / minutesToDie + 1
        result = 0
        
        while totolTest ** result < buckets:
            result += 1
            
        return result


if __name__ == "__main__":
    solution = Solution()
    print(solution.poorPigs(1000, 15, 60))
    print(solution.poorPigs(1, 1, 1))