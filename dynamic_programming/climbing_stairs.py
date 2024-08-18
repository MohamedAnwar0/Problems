class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n ==2: return n
        return self.climbStairs(n-2) + self.climbStairs(n-1)
        

def climb(n):
    if n ==1 or n ==2 :
        return n
    preprev = 1
    prev = 2
    current = 0
    for i in range(3,n+1):
        current = prev + preprev
        preprev = prev
        prev = current
    return current
