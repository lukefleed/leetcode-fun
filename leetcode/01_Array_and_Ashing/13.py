class Solution:
    def romanToInt(self, s: str) -> int:

        # 1. Create a dictionary to store the values of each roman numeral
        roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        # 2. Create a variable to store the total value
        total = 0

        # 3. Loop through the string
        for i in range(len(s)):
            # 4. If the current value is less than the next value, subtract the current value from the total
            if i < len(s) - 1 and roman_dict[s[i]] < roman_dict[s[i + 1]]:
                total -= roman_dict[s[i]]
            # 5. If the current value is greater than or equal to the next value, add the current value to the total
            else:
                total += roman_dict[s[i]]

        return total
