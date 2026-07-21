class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        t = '1' + s + '1'
        n = len(t)
        
        # Build run-length encoding of t
        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and t[j] == t[i]:
                j += 1
            runs.append((t[i], j - i))
            i = j
        
        ones = s.count('1')
        max_gain = 0
        
        # Interior '1'-runs (not first or last run) are always 
        # surrounded by '0'-runs on both sides, since runs alternate
        # and t starts/ends with '1'.
        for idx in range(1, len(runs) - 1):
            if runs[idx][0] == '1':
                gain = runs[idx - 1][1] + runs[idx + 1][1]
                if gain > max_gain:
                    max_gain = gain
        
        return ones + max_gain