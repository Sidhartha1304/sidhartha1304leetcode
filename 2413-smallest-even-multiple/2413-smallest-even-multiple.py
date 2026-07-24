class Solution(object):
    def smallestEvenMultiple(self, n):
       if(n%2==0):
            return n
       elif(n%2!=0):
            n*=2
            return n
        