class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        rst=0
        hlst=[]
        ilst=[] # Keep track of the starting index instead of the width, so we don't need to update the width everytime
        for i in xrange(len(height)):
            index=i
            while hlst and hlst[-1]>height[i]:
                index=ilst.pop() # Need to get the index of the last pop, so update it in every loop
                area=hlst.pop()*(i-index)
                rst=area if area>rst else rst
            if not hlst or height[i]!=hlst[-1]:
                hlst.append(height[i])
                ilst.append(index) # Need to take the width of the popped triangle into consideration
        for i in xrange(len(hlst)):
            area=hlst[i]*(len(height)-ilst[i])
            rst=area if area>rst else rst
        return rst