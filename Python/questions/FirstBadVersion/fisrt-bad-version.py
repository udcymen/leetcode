def firstBadVersion(self, n) -> int:
    start, end = 1, n
        
    while start + 1 < end:
        mid = (start + end) // 2
        
        if isBadVersion(mid):
            end = mid
        else:
            start = mid
            
    if isBadVersion(start):
        return start
    
    return end
