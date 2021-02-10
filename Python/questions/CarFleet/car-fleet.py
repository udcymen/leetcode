class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if not target or not position or not speed:
            return 0
        
        cars = sorted(zip(position, speed))
        times = [float(target - p) / s for p, s in cars]
        result = 0
        
        while len(times) > 1:
            head = times.pop()
            
            if head < times[-1]:
                result += 1
            else:
                times[-1] = head
                
        return result + len(times)