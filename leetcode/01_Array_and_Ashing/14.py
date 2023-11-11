class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # 1. Check if the list is empty
        if not strs:
            return ""

        # 2. Find the shortest string in the list
        shortest_str = min(strs, key=len)

        # 3. Loop through the shortest string
        for i, char in enumerate(shortest_str):
            for other in strs:
                if other[i] != char:
                    return shortest_str[:i]

        return shortest_str
        
        
        
