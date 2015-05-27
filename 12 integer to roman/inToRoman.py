class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        result=''
        k=num/1000
        for i in xrange(k):
            result+='M'
        r=num%1000
        h=r/100
        if h<4:
            for i in xrange(h):
                result+='C'
        elif h==4:
            result+='CD'
        elif h<9:
            result+='D'
            for i in xrange(h-5):
                result+='C'
        else:
            result+='CM'
        r=r%100
        t=r/10
        if t<4:
            for i in xrange(t):
                result+='X'
        elif t==4:
            result+='XL'
        elif t<9:
            result+='L'
            for i in xrange(t-5):
                result+='X'
        else:
            result+='XC'
        r=r%10
        s=r
        if s<4:
            for i in xrange(s):
                result+='I'
        elif s==4:
            result+='IV'
        elif s<9:
            result+='V'
            for i in xrange(s-5):
                result+='I'
        else:
            result+='IX'
        
        return result