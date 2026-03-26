class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        # first = ways to reach step 1, second = ways to reach step 2
        first, second = 1, 2
        
        for i in range(3, n + 1):
            # The current step is the sum of the previous two
            current = first + second
            first = second
            second = current
            
        return second