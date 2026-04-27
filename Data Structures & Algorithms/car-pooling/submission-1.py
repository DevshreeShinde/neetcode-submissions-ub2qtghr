class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        events=[]
        for trip in trips:
            events.append([trip[1],trip[0]])
            events.append([trip[2],-trip[0]])
        curr = 0
        events.sort()
        for event in events:
            curr+=event[1]
            if curr>capacity:
                return False
        return True
