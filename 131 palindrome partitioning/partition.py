class Solution:
    result=[]
    # @param {string} s
    # @return {string[][]}
    def partition(self, s):
        self.result=[] # need to use self to refer the global variable 
        if not s:
            return None
        self.partitionHelper(s,[])
        return self.result
    def partitionHelper(self,input,l):
        if not input:
            self.result.append(l)
            return
        for i in xrange(1,len(input)+1):
            if input[:i] == input[i-1::-1]:
                newList=list(l)
                newList.append(input[:i])
                self.partitionHelper(input[i:],newList)