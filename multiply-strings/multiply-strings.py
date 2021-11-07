class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1=="0" or num2=="0":
            return "0"
        N=len(num1)+len(num2)
        ans=[0]*N
        
        first_num = num1[::-1]
        second_num=num2[::-1]
        
        for place2, digit2 in enumerate(second_num):
            for place1, digit1 in enumerate(first_num):
                num_zeros = place1 + place2
                
                carry = ans[num_zeros]
                multiplication = int(digit1)*int(digit2)+carry
                
                ans[num_zeros] = multiplication % 10 
                
                ans[num_zeros+1] += multiplication // 10
                
        if ans[-1]==0:
            ans.pop()
            
        return ''.join(str(digit) for digit in reversed(ans))
        