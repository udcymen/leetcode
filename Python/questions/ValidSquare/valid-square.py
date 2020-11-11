class Solution:
    def distant(self, p1: list[int], p2: list[int]):
        return (p2[0] - p1[0]) * (p2[0] - p1[0]) + (p2[1] - p1[1]) * (p2[1] - p1[1])
    
    def validSquare(self, p1: list[int], p2: list[int], p3: list[int], p4: list[int]) -> bool:
        p1, p2, p3, p4 = sorted([p1, p2, p3, p4])
        
        return self.distant(p1, p2) > 0 and \
            self.distant(p1, p2) == self.distant(p2, p4) and \
            self.distant(p2, p4) == self.distant(p4, p3) and \
            self.distant(p4, p3) == self.distant(p3, p1) and \
            self.distant(p2, p3) == self.distant(p1, p4)


if __name__ == "__main__":
    solution = Solution()
    print(solution.validSquare([0,0], [1,1], [1,0], [0,1]))
    print(solution.validSquare([0,0], [1,1], [1,0], [1,1]))
