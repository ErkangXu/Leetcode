class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        volume=0
        i=1
        length=len(height)
        while i<length:
            if height[i]<height[i-1]:
                j=i
                maxV=0
                maxI=i
                while j<length and height[j]<height[i-1]:
                    if height[j]>maxV:
                        maxV=height[j]
                        maxI=j
                    j+=1
                if j==length:
                    next=maxI
                    top=height[maxI]
                else:
                    next=j
                    top=height[i-1]
                for k in xrange(i,next):
                    volume+=top-height[k]
                i=next
            i+=1
        return volume