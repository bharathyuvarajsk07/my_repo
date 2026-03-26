class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Special cases:
        # 1. x < 0 is never a palindrome.
        # 2. x > 0 ending in 0 is never a palindrome.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_number = 0
        while x > reverted_number:
            # Move the last digit of x to the end of reverted_number
            reverted_number = reverted_number * 10 + x % 10
            x //= 10

        # When the length is odd, we can get rid of the middle digit by 
        # reverted_number // 10. For example, for 121, x = 1, reverted_number = 12.
        return x == reverted_number or x == reverted_number // 10