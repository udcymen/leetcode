class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minutesDegree = minutes * 6 % 360
        hourDegree = (hour + minutesDegree / 360) * 30 % 360
        
        result = abs(hourDegree - minutesDegree)

        return min([360 - result, result])
