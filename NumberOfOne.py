# coding=utf-8
class Solution:
    def NumberOf1(x):
        num = 0
        for i in range(0, 32):
            if x & 1:
                num = num + 1
            x = x >> 1
        return num


n = input("Please enter the number you want to count:\n")
n = int(n)
print(Solution.NumberOf1(n))