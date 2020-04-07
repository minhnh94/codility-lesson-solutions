def solution(a):
    a.sort()
    start = 0
    end = len(a) - 1
    min_sum = 2000000000
    while start <= end:
        calc_sum = a[start] + a[end]
        min_sum = min(min_sum, abs(calc_sum))
        if calc_sum < 0:
            start += 1
        elif calc_sum > 0:
            end -= 1
        else:
            return 0

    return min_sum
