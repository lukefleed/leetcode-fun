class Solution:
    def strToInt(self, num: str) -> int:
        multiplier = 1
        ans = 0
        for each in reversed(num):
            ans += multiplier * (ord(each) - ord('0'))
            multiplier *= 10

        return ans

    def multiply(self, num1: str, num2: str) -> str:
        return str(self.strToInt(num1) * self.strToInt(num2))
    
    
