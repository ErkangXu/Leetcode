class Solution:
    # @param {integer[][]} matrix
    # @return {integer[]}
    def spiralOrder(self, matrix):
        result =[]
        if not matrix:
            return []
        rowN=len(matrix)
        colN=len(matrix[0])
        ite_bound=(rowN+1)/2 if rowN<colN else (colN+1)/2
        for i in xrange(ite_bound):
            row_upper_bound=i
            row_lower_bound=rowN-1-i
            col_left_bound=i
            col_right_bound=colN-1-i
            for j in xrange(col_left_bound,col_right_bound+1):
                result.append(matrix[row_upper_bound][j])
            for j in xrange(row_upper_bound+1,row_lower_bound+1):
                result.append(matrix[j][col_right_bound])
            if row_upper_bound != row_lower_bound: # If it's single row, should not count twice
                for j in xrange(col_right_bound-1,col_left_bound-1,-1):
                    result.append(matrix[row_lower_bound][j])
            if col_left_bound != col_right_bound:
                for j in xrange(row_lower_bound-1,row_upper_bound,-1):
                    result.append(matrix[j][col_left_bound])
        return result