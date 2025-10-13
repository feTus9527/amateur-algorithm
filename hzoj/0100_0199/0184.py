"""
See: https://oj.haizeix.com/problem/184
"""

n = int(input("Please input a positive integer.\n"))


def fn_recursively(x: int) -> int:
    if x == 1:
        return 1
    return (fn_recursively(x - 1) + 1) * 2


def fn_iteratively(x: int) -> int:
    result = 1
    for _ in range(1, x):
        result = (1 + result) * 2
    return result


print("recursive function result:", fn_recursively(n))
print("iterate function result:", fn_iteratively(n))
