class Solution:
    record=[]
    counter=0
    rowN=0
    columnN=0
    def helper(self, row, column):
        self.record[row][column]='2'
        if column>0 and self.record[row][column-1]=='1':
            self.helper(row,column-1)
        if column+1<self.columnN and self.record[row][column+1]=='1':
            self.helper(row,column+1)
        if row>0 and self.record[row-1][column]=='1':
            self.helper(row-1,column)
        if row+1<self.rowN and self.record[row+1][column]=='1':
            self.helper(row+1,column)
    # @param {character[][]} grid
    # @return {integer}
    def numIslands(self, grid):
        if not grid:
            return 0
        self.record=grid
        self.rowN=len(grid)
        self.columnN=len(grid[0])
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if self.record[i][j]=='1':
                    self.counter+=1
                    self.helper(i,j)
        return self.counter
                    