class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        #XOR연산_다르면 1, 같으면0
        return bin(x^y).count('1')