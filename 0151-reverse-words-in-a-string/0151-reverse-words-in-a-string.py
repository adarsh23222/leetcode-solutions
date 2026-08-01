class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)
        words= s.split()
        return " ".join(reversed(words))

        
        

        