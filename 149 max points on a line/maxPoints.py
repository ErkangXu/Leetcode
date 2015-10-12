# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        length=len(points)
        if length<3:
            return length
        maxo=2
        for i in xrange(len(points)):
            p=points[i]
            dic={}
            samePointC=0 # Need to count the how many following points are the same, and add it into the angle count
            infinityCount=0 # Can't divide by 0, so have a seperate count
            for j in xrange(i+1,len(points)):
                q=points[j]
                if p.x==q.x:
                    if p.y==q.y:
                        samePointC+=1
                    else:
                        infinityCount+=1
                else:
                    ang=(p.y-q.y)/float(p.x-q.x)
                    if ang not in dic:
                        dic[ang]=1
                    else:
                        dic[ang]=dic[ang]+1
            maxi=0 # This is the following points count, not including the leading point
            for k,v in dic.iteritems():
                if v>maxi:
                    maxi=v
            maxi=max(maxi,infinityCount)
            maxi+=samePointC
            maxi+=1 # add the leading point in
            if maxi>maxo:
                maxo=maxi
        return maxo