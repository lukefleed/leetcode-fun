class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        i = 0 
        while i < len(s):
            if s.count(s[i]) == 1:
                return i
            i += 1
            
        return -1
      
        
