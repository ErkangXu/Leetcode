class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
        sum=0
        start=0
        leftG=0
        for i in xrange(len(gas)):
            diff=gas[i]-cost[i]
            leftG+=diff
            sum+=diff
            if sum<0: # even if sum==0, I should not move start, because solution is guaranteed to be unique, sum==0 happens when len=1
                start=i+1
                sum=0
        if leftG<0:
            return -1
        else:
            return start