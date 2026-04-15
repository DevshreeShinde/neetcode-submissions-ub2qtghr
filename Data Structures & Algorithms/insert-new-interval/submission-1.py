class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        j=0
        while j<len(intervals) and intervals[j][1]<newInterval[0]:
            j+=1
        k=j
        start,end=newInterval
        while j<len(intervals) and intervals[j][0]<=end:
            start=min(intervals[j][0],start)
            end=max(intervals[j][1],end)
            j+=1
        intervals[k:j]=[[start,end]]
        return intervals
        