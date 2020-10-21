class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        #前面的執行結果a + b...的b部分
        operand = 0
        #前面的執行結果a + b...的a部分
        res = 0
        #前面的執行結果a + b...的運算子部分
        sign = 1

        for ch in s:
            if ch.isdigit():

                operand = (operand * 10) + int(ch)

            elif ch == '+':
                #a + b + c, 代碼執行到第二個加號, 將a + b計算, 保存在res
                res += sign * operand
                sign = 1
                operand = 0

            elif ch == '-':
                #a + b - c, 代碼執行到第二個減號, 將a + b計算, 保存在res
                res += sign * operand
                sign = -1
                operand = 0

            elif ch == '(':
                #1. a + (b + ...), 代碼執行到第一個(號, 把a部分(即res)放到stk, 把在a之後的第一個運算子放到stk, 此時operand為0
                #
                #2. a + (b + (c + ...)...), 代碼執行到第二個(號, 此時stk有a, +, 
                #   res = b, res在第一次遇到(時已經被清空為0, 接著遇到b, operand變成b, 遇到第二個+號後res=b,
                #   保存b和b後面的加號到stk, stk會長得像a, +, b, +
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0

            elif ch == ')':
                #1. a + (b1 + b2 + b3), res保存的是b1+b2的計算結果, 然後再把b3給加上去(下面執行過後)
                res += sign * operand

                #將(前面的運算子pop出來, 也就是a後面的運算子
                res *= stack.pop() # stack pop 1, sign

                #將a和res相加
                res += stack.pop() # stack pop 2, operand

                operand = 0

        #因為(會配), 所以不用考慮剩下的), stk最後只會剩空
        return res + sign * operand