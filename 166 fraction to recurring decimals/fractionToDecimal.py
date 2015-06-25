class Solution:
    # @param {integer} numerator
    # @param {integer} denominator
    # @return {string}
    def fractionToDecimal(self, numerator, denominator):
        product=numerator*denominator
        abs_denominator=abs(denominator)
        integer=abs(numerator)//abs_denominator
        left_over=abs(numerator)%abs_denominator 
        result='-'+str(integer) if product<0 else str(integer) # numerator or denominator might be nagative
        if left_over==0:
            return result
        else:
            result+='.'
            dict={}
            dict[left_over]=len(result)
            while 1:
                aided=left_over*10
                digit=aided//abs_denominator
                left_over=aided%abs_denominator
                if left_over==0:
                    return result+str(digit)
                elif left_over in dict:
                    return result[:dict[left_over]] + '(' + result[dict[left_over]:] + str(digit) + ')'   # the recurring part might be more that one digit
                else:
                    result+=str(digit)
                    dict[left_over]=len(result)