class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        word_set = set(wordDict)

        # dp[i] means s[:i] can be segmented
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for end in range(1, len(s) + 1):
            for start in range(end):
                if dp[start] and s[start:end] in word_set:
                    dp[end] = True
                    break

        return dp[len(s)]