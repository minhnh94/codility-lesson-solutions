def solution(a):
    sum_left = sum(a)
    sum_right = 0
    results = []
    for i in a[:len(a) - 1]:
        sum_left -= i
        sum_right += i
        results.append(abs(sum_left - sum_right))
    return min(results)
