class Solution(object):
    def helper(self,d,board,ind,re):
        if ind==d:
            re.append(list(board)) # Need to make another copy of board
            return
        for c in xrange(d):
            flag=False
            for i in xrange(ind):
                if board[i][c]=='Q' or ( c-ind+i>=0 and board[i][c-ind+i]=='Q' ) or ( c+ind-i<d and board[i][c+ind-i]=='Q'):
                    flag=True #c+ind-1<d not <=
                    break
            if flag:
                continue
            if len(board)==ind:
                board.append('.'*c+'Q'+'.'*(d-c-1)) # Can't reasign a element that isn't there
            else:
                board[ind]='.'*c+'Q'+'.'*(d-c-1)
            self.helper(d,board,ind+1,re)
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result=[]
        self.helper(n,[],0,result)
        return result