# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def mergeSort(self,inp,start,end):
        if start<end:
            self.mergeSort(inp,start,(start+end)/2) # It's (start+end)/2 not (end-start)/2
            self.mergeSort(inp,(start+end)/2+1,end)
            
            newList=inp[start:end+1]
            tail=end-start
            mid=tail/2
            p,lp,rp=start,0,mid+1
            while lp<=mid and rp<=tail:
                if newList[lp].start<newList[rp].start:
                    inp[p]=newList[lp]
                    lp+=1
                else:
                    inp[p]=newList[rp]
                    rp+=1
                p+=1
            if rp>tail:
                while lp<=mid:
                    inp[p]=newList[lp]
                    p+=1
                    lp+=1
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        self.mergeSort(intervals,0,len(intervals)-1)
        newI=intervals[:1]
        for i in xrange(1,len(intervals)):
            if intervals[i].start>newI[-1].end:
                newI.append(intervals[i])
            else:
                if intervals[i].end>newI[-1].end:
                    newI[-1]=Interval(newI[-1].start,intervals[i].end)
        return newI