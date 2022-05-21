class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        dp = [False]*(n + 1)
        dp[0] = True
        
        for i in range(1, n + 1):
            temp = ""
            for j in range(i, n + 1):
                temp += s[j - 1]
                if temp in wordDict and dp[i - 1]:
                    dp[j] = True
        
        return dp[n]

