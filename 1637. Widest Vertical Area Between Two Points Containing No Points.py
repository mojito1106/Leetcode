class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        
        a = sorted(points)
        #print(a[1])
        diff = 0
        for i in range (len(points)-1):
            b = a[i+1][0] - a[i][0]
            if b > diff:
                diff = b
        return diff
