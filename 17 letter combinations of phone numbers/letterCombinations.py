class Solution:
    dict={
        '1':(''),
        '2':('a','b','c'),
        '3':('d','e','f'),
        '4':('g','h','i'),
        '5':('j','k','l'),
        '6':('m','n','o'),
        '7':('p','q','r','s'),
        '8':('t','u','v'),
        '9':('w','x','y','z'),
        '0':(' ')
    }
    result=[]
    bound=0
    digitString=""  # using a global variable is faster, need to assign a name otherwise cause error
    def letterHelper(self, index,list):
        for c in self.dict[self.digitString[index]]:
            newList=list[:]
            newList.append(c)  # should use round not square brackets
            if index==self.bound:
                self.result.append(''.join(newList))
            else:
                self.letterHelper(index+1,newList)
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        self.result=[]
        self.digitString=digits
        if not digits:
            return ()
        self.bound=len(digits)-1
        self.letterHelper(0,[])
        return self.result