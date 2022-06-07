class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        '''
        
        360/12 = 30
        
        in 60mins -> 30*
        1min -> 1/2 degree
        
        1/2 degree per min for hour hand
        
        
        30mins -> 180
        1min -> 180/30 = 6 degree
        
        '''
        
        hours_degree = (hour%12)*30 + minutes/2
        minutes_degree = minutes*6
        
        ans1 = abs(minutes_degree - hours_degree)
        ans2 = 360 - ans1
        
        return min(ans1, ans2)
        