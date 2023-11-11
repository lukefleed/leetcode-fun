class Solution:
    def calculate(self, s: str) -> int:

        stack = [] # stack to store numbers
        num = 0 # current number being processed
        sign = '+' # current sign being processed
        for i in range(len(s)): 
            if s[i].isdigit(): # if current character is a digit
                num = num * 10 + int(s[i]) # update current number in reverse polish notation
            if s[i] in '+-*/' or i == len(s) - 1: # if current character is a sign or last character
                if sign == '+': 
                    stack.append(num) 
                elif sign == '-': 
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop() * num) # pop last number and multiply it with current number
                elif sign == '/': 
                    stack.append(int(stack.pop() / num)) # pop last number and divide it by current number
                sign = s[i]
                num = 0
        return sum(stack)


        
 
