def solution(n, a):
    counters = [0] * n
    max_counter = 0
    current_max_val = 0
    for i in a:
        if i != n + 1:
            counters[i - 1] = max(max_counter, counters[i - 1]) + 1
            current_max_val = max(current_max_val, counters[i - 1])
        else:
            max_counter = current_max_val

    for i in range(len(counters)):
        counters[i] = max(max_counter, counters[i])

    return counters
