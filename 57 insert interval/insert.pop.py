# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def helper(self, val, intervals):
        start,end=0,len(intervals)-1
        while start<=end:
            mid=(start+end)/2
            if intervals[mid].start<val:
                start=mid+1
            elif intervals[mid].start>val:
                end=mid-1
            else:
                return mid
        return end
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            intervals.append(newInterval)
            return intervals
        front=self.helper(newInterval.start, intervals)
        end=self.helper(newInterval.end, intervals)
        if front!=-1 and intervals[front].end>=newInterval.start:
            if intervals[end].end<=newInterval.end:
                intervals[front].end=newInterval.end
            else:
                intervals[front].end=intervals[end].end
            count=end-front
            while count>0:
                intervals.pop(front+1)
                count-=1
        else:
            if front<len(intervals)-1: 
                if newInterval.end<intervals[front+1].start: # The new interval fits in the gap
                    intervals.insert(front+1, newInterval)
                    return intervals
                intervals[front+1].start=newInterval.start
                if intervals[end].end<=newInterval.end:
                    intervals[front+1].end=newInterval.end
                else:
                    intervals[front+1].end=intervals[end].end
                count=end-front-1
                while count>0:
                    intervals.pop(front+2)
                    count-=1
            else: # It could be suitable in the tail
                intervals.append(newInterval)
        return intervals