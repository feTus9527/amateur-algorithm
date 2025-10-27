"""
See: https://oj.haizeix.com/problem/235
"""

n = int(input())

container = [0] * 10


def fn(i: int, j: int, n: int) -> None:
    if j > n:
        return
    for k in range(j, n + 1):
        container[i] = k
        for l_i, l in enumerate(range(i + 1)):
            if container[l] != 0:
                print(container[l], end="" if l_i == i else " ")

        print()
        fn(i + 1, k + 1, n)


fn(0, 1, n)
