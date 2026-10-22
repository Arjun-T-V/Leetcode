class Solution:
    def isPalindrome(self, n: int) -> bool:
        return str(n)==str(n)[::-1]
        
