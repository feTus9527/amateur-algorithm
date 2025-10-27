"""
See: https://oj.haizeix.com/problem/237
"""

n = int(input())


def fn(n: int, current=None, remaining=None) -> None:
    if current is None:
        current = []
        remaining = list(range(1, n + 1))
    if not remaining:
        for i, item in enumerate(current):
            print(item, end="" if i == len(current) - 1 else " ")
        print()
        return
    for i in range(len(remaining)):
        new_current = current + [remaining[i]]
        new_remaining = remaining[:i] + remaining[i + 1 :]
        fn(n, new_current, new_remaining)


fn(n)
