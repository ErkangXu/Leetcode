class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        dividendA=dividend if dividend>=0 else -dividend
        rem=dividendA
        divisorA=divisor if divisor>0 else -divisor
        mulS=0
        while (rem>=divisorA): # Condition need the : sign
            close=divisorA
            mul=1
            while(rem-close>close): # Should use rem here instead of dividendA
                close<<=1
                mul<<=1
            rem=rem-close
            mulS+=mul
        result=0
        if (dividend>=0 and divisor>0): # Can't write condition and execution in the same line
            result = mulS 
        elif (dividend>=0 and divisor<0): # python uses elif instead of else if
            result = -mulS  # When one of the operand is negative, just add a - sign
        elif (dividend<0 and divisor>0):
            result = -mulS 
        else:          # Need : even afte else 
            result = mulS 
        if result>2147483647:
            return 2147483647     # Python's integer has much larger range, so the sum will not decrease 
        elif result<-2147483648:
            return -2147483648
        else:
            return result