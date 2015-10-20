class Solution(object):
    def helper(self,d,board,ind,lis,re):
        if ind==d:
            re.append(list(board)) # Need to make another copy of board
            return
        choices={ i for i in xrange(d) }
        for i in xrange(ind):
            choices.discard(lis[i])
            choices.discard( lis[i]-(ind-i) )
            choices.discard( lis[i]+(ind-i) )
        for c in choices:
            if len(lis)==ind:
                board.append('.'*c+'Q'+'.'*(d-c-1)) # Can't reasign a element that isn't there
                lis.append(c)
            else:
                board[ind]='.'*c+'Q'+'.'*(d-c-1)
                lis[ind]=c
            self.helper(d,board,ind+1,lis,re)
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result=[]
        self.helper(n,[],0,[],result)
        return result