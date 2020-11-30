class Solution:
    def maxDepth(self, s: str) -> int:
        flag = 0
        count = 0
        max_c = 0
        for i in range(len(s)):
            if s[i] =='(':
                #count += 1 #2 1 2 
                flag += 1 #2 2 3
            if s[i] == ')':
                if flag > max_c:
                    max_c = flag #2 3 
                #count = 0 #0 0
                if flag > 0: 
                    flag -= 1 #1 2 1
                  
                  
                
        if (flag == 0) and (max_c == 0):
            return 0
        else: return max_c

        
#version 2     
"""class Solution:
    def maxDepth(self, s: str) -> int:
        max_val = 0
        open_bracket = 0
        for c in s:
            if c == '(':
                open_bracket += 1
            
            if c == ')':
                max_val = max(open_bracket, max_val)
                open_bracket -= 1
                
        return max_val"""
