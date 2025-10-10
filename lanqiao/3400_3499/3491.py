"""
See: https://www.lanqiao.cn/problems/3491/learning/
"""


def digit_count(num: int) -> int:
    cnt = 0
    while num > 0:
        cnt += 1
        num //= 10
    return cnt


def is_lucky_number(num: int, digits: int) -> bool:
    half = digits // 2
    left, right = 0, 0
    for i in range(1, digits + 1):
        d = num % 10
        if i <= half:
            left += d
        else:
            right += d
        num //= 10
    return left != 0 and left == right


result = 0
for i in range(10, 100000001):
    digits = digit_count(i)
    if digits & 1 != 0:
        continue
    if is_lucky_number(i, digits):
        result += 1
# 4430091
print(result)
