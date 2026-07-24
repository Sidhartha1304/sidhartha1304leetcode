class Solution(object):
    def differenceOfSums(self, n, m):
        divisiblesum=0
        nondivisiblesum=0
        for i in range(1,n+1):
            if(i%m==0):
                divisiblesum+=i
            elif(i%m!=0):
                nondivisiblesum+=i
        return nondivisiblesum-divisiblesum