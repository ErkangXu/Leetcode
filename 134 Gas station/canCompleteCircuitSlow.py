class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
        le=len(gas)
        if le==1:
            return 0 if gas[0]>=cost[0] else -1
        for x in xrange(le):
            su=0
            y=x
            while y < le:
                su+=gas[y]-cost[y]
                if(su<0):
                    break
                else: 
                    y+=1
            if y==le:
                y=0
                while(y<x):
                    su+=gas[y]-cost[y]
                    if(su<0):
                        break
                    else:
                        y+=1
            else:
                continue
            if y==x:
                return x
        return -1