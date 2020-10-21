class Solution(object):
    def isMatch(self, text, pattern):
        dp = [False] * (len(pattern) + 1)
        dp = [dp.copy() for _ in range(len(text)+1)]
        
        dp[-1][-1] = True
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):
                first_match = i < len(text) and pattern[j] in {'.', text[i]}
                if j + 1 < len(pattern) and pattern[j + 1] == '*':
                    dp[i][j] = dp[i][j+2] or (first_match and dp[i+1][j])
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
                    
                print((i, j), dp[i][j])
        return dp[0][0]
        
#top-down
#初始dp[-1][-1] = True, 表示2者都為空字串, 其匹配結果為True