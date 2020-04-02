def solution(a, b, k):
    if a % k == 0 or b % k == 0:
        return (b - a) // k + 1
    else:
        return (b - (a - a % k)) // k
