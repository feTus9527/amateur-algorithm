"""
See: https://www.lanqiao.cn/problems/19709/learning/
"""

num = int(input())
result = 0
for i in range(1, num + 1):
    while i > 0:
        if i % 2 != 0:
            i //= 10
        else:
            break
        if i % 2 == 0:
            i //= 10
        else:
            break
    if i == 0:
        result += 1
print(result)
