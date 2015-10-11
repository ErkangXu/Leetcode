class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0
        count=1
        last=1
        i=1
        while i < len(ratings):
            if ratings[i]>ratings[i-1]:
                last+=1
                count+=last
            elif ratings[i]==ratings[i-1]:
                last=1 # If two kids have equal ratings, one kid can have less candy, we can drop it to 1
                count+=last  
            else:
                num=0
                while i<len(ratings) and ratings[i]<ratings[i-1]:
                    num+=1
                    i+=1
                if num>=last:
                    count+=num+1-last #need to add this much to last position first
                count+=(num+1)*num/2 #need to add the area of the triangle
                last=1
                i-=1 # need to subtract 1 to neutalize the affect of increment
            i+=1
        return count