class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return 0
        if len(nums)==2:
            return nums[1]-nums[0]
        mini,maxi=nums[0],nums[0]
        for n in nums:
            if n<mini:
                mini=n
            elif n>maxi:
                maxi=n
        if mini==maxi:
            return 0
        unit=(maxi-mini)/(len(nums)-1)
        if (maxi-mini)%(len(nums)-1)!=0:
            unit+=1
        ll=[[] for i in xrange(len(nums))] # In case of the [1,2,3,100] situation, make len(nums) buckets
        for n in nums:
            ll[(n-mini)/unit].append(n)
        sec=[(0,0)]
        i=0
        while not ll[i]:
            i+=1
        j=i+1
        while not ll[j]:
            j+=1
        fir=[(i,j)]
        i=j
        while j<len(nums):
            j+=1
            while j<len(nums) and not ll[j]:
                j+=1
            if j==len(nums):
                break
            if j-i>fir[0][1]-fir[0][0]:
                sec=fir
                fir=[(i,j)]
            elif j-i==fir[0][1]-fir[0][0]:
                fir.append((i,j))
            elif j-i==sec[0][1]-sec[0][0]:
                sec.append((i,j))
            i=j
        gap=0
        for tu in fir:
            g=sorted(ll[tu[1]])[0]-sorted(ll[tu[0]])[-1]
            gap=g if g>gap else gap
        if sec==[(0,0)] or fir[0][1]-fir[0][0]>sec[0][1]-sec[0][0]+1:
            return gap
        else:
            for tu in sec:
                g=sorted(ll[tu[1]])[0]-sorted(ll[tu[0]])[-1]
                gap=g if g>gap else gap
            return gap
            