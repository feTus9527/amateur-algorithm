"""
See: https://oj.haizeix.com/problem/236
"""

[n, m] = [int(item) for item in input().split(" ")]

container = []


def fn(min_val: int, n: int, m: int) -> None:
    if m == 0:
        for i, item in enumerate(container):
            print(item, end="" if i == len(container) - 1 else " ")
        print()
        return
    for i in range(min_val, n):
        container.append(i + 1)
        fn(i + 1, n, m - 1)
        container.pop()


fn(0, n, m)
