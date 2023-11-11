class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        n = len(haystack)
        m = len(needle)
        
        if m > n:
            return -1
        
        i = 0
        while i <= n-m:
            if haystack[i:i+m] == needle:
                return i
            i += 1

        return -1
        
        
