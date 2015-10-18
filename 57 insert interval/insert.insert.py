# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            intervals.append(newInterval)
            return intervals
        start,end=0,len(intervals)-1
        while start<=end:
            mid=(start+end)/2
            if intervals[mid].end<newInterval.start:
                start=mid+1
            elif intervals[mid].end>newInterval.start:
                end=mid-1
            else:
                end=mid-1
                break
        left=end
        start,end=0,len(intervals)-1
        while start<=end:
            mid=(start+end)/2
            if intervals[mid].start<newInterval.end:
                start=mid+1
            elif intervals[mid].start>newInterval.end:
                end=mid-1
            else:
                start=mid+1
                break
        right=start
        result=[]
        for i in xrange(left+1):
            result.append(intervals[i])
        lb=newInterval.start if left==len(intervals)-1 else min(newInterval.start,intervals[left+1].start)
        rb=newInterval.end if right==0 else max(newInterval.end,intervals[right-1].end)
        insert = Interval(lb,rb)
        result.append(insert)
        for i in xrange(right,len(intervals)):
            result.append(intervals[i])
        return result