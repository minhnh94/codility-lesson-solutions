from collections import deque


def solution(a, k):
    a = deque(a)
    a.rotate(k)
    return list(a)
