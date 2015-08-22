class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        rowN=len(matrix)
        colN=len(matrix[0])
        hList=[0 for i in xrange(colN)]
        lBoundL=[0 for i in xrange(colN)]
        rBoundL=[colN for i in xrange(colN)] # use colN here so we don't need to add 1 afterwards
        maxArea=0
        for i in xrange(rowN):
            cur_left=0
            for j in xrange(colN):
                if matrix[i][j]=='1':
                    hList[j]+=1
                    lBoundL[j]=max(lBoundL[j],cur_left)
                else:
                    hList[j]=0
                    lBoundL[j]=0
                    cur_left=j+1
            cur_right=colN
            for j in xrange(colN-1,-1,-1):
                if matrix[i][j]=='1':
                    rBoundL[j]=min(rBoundL[j],cur_right)
                    maxArea=max(maxArea,hList[j]*(rBoundL[j]-lBoundL[j])) # Put it here so can skip height=0 situation
                else:
                    rBoundL[j]=colN
                    cur_right=j
        return maxArea