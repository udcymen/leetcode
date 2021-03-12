class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or len(coins) == 0:
            return -1
        
        if amount == 0:
            return 0
        
        result = 0
        visited = set()
        q = [amount]
        
        while q:
            result += 1
            
            for i in range(len(q)):
                remain = q.pop(0)

                for c in coins:
                    r = remain - c
                    
                    if r in visited:
                        continue
                    
                    visited.add(r)
                    
                    if r == 0:
                        return result
                    elif r > 0:
                        q.append(r)
        
        return -1