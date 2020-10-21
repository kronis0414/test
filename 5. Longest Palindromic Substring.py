class Solution:
    def longestPalindrome(self, s):
        res = ''
        for i in range(len(s)):
            tmp = ''
            #case 1
            tmp = self.run(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            #case 2
            tmp = self.run(s, i, i+1)
            if len(tmp) > len(res):
                res = tmp
        return res
    def run(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
#從左到右一個一個字元檢視他是否是迴文, 
#分成
#case 1.以自己為中心向2側擴展, 
#  如zyxaxyz, 從a開始檢查, 接著檢查xx是否相同
#case 2.兩個相同字元向2側擴展
#  如zyxxyz, 從xx開始檢查, 接著檢查yy是否相同
