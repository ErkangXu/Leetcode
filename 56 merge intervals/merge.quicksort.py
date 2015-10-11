# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def quickSort(self,inp,start,end):
        if start>=end:
            return
        else:
            pickV=inp[(start+end)/2].start
            lp,rp=start,end
            while lp<=rp:
                while inp[lp].start<pickV:
                    lp+=1
                while inp[rp].start>pickV: # Can't use = here, leave all the duplication in the middle
                    rp-=1
                if lp>rp:
                    break
                inp[lp],inp[rp]=inp[rp],inp[lp]
                lp+=1
                rp-=1 
            self.quickSort(inp,start,lp-1) # It's (start+end)/2 not (end-start)/2
            self.quickSort(inp,lp,end)
            
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        self.quickSort(intervals,0,len(intervals)-1)
        newI=intervals[:1]
        for i in xrange(1,len(intervals)):
            if intervals[i].start>newI[-1].end:
                newI.append(intervals[i])
            else:
                if intervals[i].end>newI[-1].end:
                    newI[-1]=Interval(newI[-1].start,intervals[i].end)
        return newI