class Solution(object):
    def helper(self,index,rl,col,bd,rs,cs,ss):
        if index==len(rl):
            return True
        i=rl[index]
        j=col[index]
        choices=rs[i].intersection(cs[j],ss[i/3][j/3])
        for c in choices:
            rs[i].remove(c)
            cs[j].remove(c)
            ss[i/3][j/3].remove(c)
            bd[i][j]=c
            if self.helper(index+1,rl,col,bd,rs,cs,ss):
                return True
            else:
                rs[i].add(c)
                cs[j].add(c)
                ss[i/3][j/3].add(c)
        return False
            
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        rowList=[]
        colList=[]
        rowSets=[{'1','2','3','4','5','6','7','8','9'} for i in xrange(9)]
        colSets=[{'1','2','3','4','5','6','7','8','9'} for i in xrange(9)]
        squareSets=[[{'1','2','3','4','5','6','7','8','9'} for i in xrange(3)] for j in xrange(3)]
        for i in xrange(9):
            for j in xrange(9):
                ch=board[i][j]
                if ch!='.':
                    rowSets[i].remove(ch)
                    colSets[j].remove(ch)
                    squareSets[i/3][j/3].remove(ch)
                else:
                    rowList.append(i)
                    colList.append(j)
        
        self.helper(0,rowList,colList,board,rowSets,colSets,squareSets)