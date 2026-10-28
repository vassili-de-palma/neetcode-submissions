from functools import cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        words = set(wordDict)
        @cache
        def rec(s):
            if s == "":
                return True 
            w = ""
            for i, c in enumerate(s):
                w += c
                if w in words:
                    if rec(s[i+1:]): 
                        return True 
            return False
        return rec(s)
            
                

        

        