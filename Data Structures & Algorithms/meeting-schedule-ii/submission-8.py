"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if intervals == []:
            return 0
        intervals = sorted(intervals, key=lambda x: x.start)
        ends=[intervals[0].end]
        ans=1
        for i in range(1,len(intervals)):
            ends = [e for e in ends if e > intervals[i].start]
            ends.append(intervals[i].end)
            ans=max(ans,len(ends))
        return ans