class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        rowN=len(matrix)
        colN=len(matrix[0])
        intMatrix=[[0 for x in xrange(colN)] for y in xrange(rowN)]
        for i in xrange(rowN):
            if matrix[i][0]=='1':
                intMatrix[i][0]=1
            for j in xrange(1,colN):
                if matrix[i][j]=='1':
                    intMatrix[i][j]=1
                if intMatrix[i][j]!=0 and intMatrix[i][j-1]!=0:
                    intMatrix[i][j]+=intMatrix[i][j-1]
        maxArea=0
        for j in xrange(colN):
            lengthSet=set()
            for i in xrange(rowN):
                if intMatrix[i][j] not in lengthSet:
                    lengthSet.add(intMatrix[i][j])
            lengthSet.discard(0)
            for length in lengthSet:
                i=0
                while i<rowN:
                    while i<rowN and intMatrix[i][j]<length:
                        i+=1
                    if i<rowN:
                        width=1
                        i+=1
                        while i<rowN and intMatrix[i][j]>=length:
                            width+=1
                            i+=1
                        tempArea=width*length
                        if tempArea>maxArea:
                            maxArea=tempArea
        return maxArea