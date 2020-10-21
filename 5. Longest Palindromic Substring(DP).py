#從字串後面去檢查是否為回文
class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        memo = [False] * n
        memo = [memo.copy() for _ in range(n)]
        
        for i in range(n):
            memo[i][i] = True
            
        startI = 0
        leng = 1
            
        for i in range(n-1,-1,-1):
            for dist in range(1, n - i):
                j = i + dist
                memo[i][j] = s[i] == s[j] if dist == 1 else (s[i] == s[j]) and memo[i+1][j-1]
                
                if memo[i][j] and j - i + 1 > leng:
                    startI = i
                    leng = j - i + 1
        return s[startI: startI + leng]
#len = 8
#i = 4
#dist = 1 to 3
#4 + 1
#4 + 2
#4 + 3

# i = 7
# do nothing

# i = 6
# abcdefgh
#       xx

# i = 5
# abcdefgh
#      xx
#      x x

# i = 4
# abcdefgh
#     xx
#     x x
#     x  x

#從字串前面去檢查是否為回文
class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        memo = [False] * n
        memo = [memo.copy() for _ in range(n)]

            
        lstart = 0
        llen = 1
  
        for end in range(n):
            for start in range(0, end+1):
                memo[start][end] = s[start] == s[end] if end-start <= 1 else (s[start] == s[end] and memo[start+1][end-1])
                if memo[start][end] and (end - start + 1) > llen:
                    lstart = start
                    llen = end - start + 1  
        return s[lstart:lstart+llen]
ss = 'cbbd'
s = Solution()
print(s.longestPalindrome(ss))
#用一個矩陣儲存狀態memo[i,j], 代表字串s[i:j+1](索引i到j)是否為回文
#若memo[i+1, j-1]是回文, 且s[i] == s[j] 則memo[i,j]也是回文, 如行16
#從字串後面開始去檢查是否為回文
# len = 8
# end = 0
# start = 0 to 0
# abcdefgh
# x

# end = 1
# start = 0 to 1
# abcdefgh
# xx
#  x

# end = 2
# start = 0 to 2
# abcdefgh
# x x
#  xx
#   x

# end = 3
# start = 0 to 3
# abcdefgh
# x  x
#  x x
#   xx
#    x

# end = 4
# start = 0 to 4
# abcdefgh
# x   x
#  x  x
#   x x
#    xx
#     x

