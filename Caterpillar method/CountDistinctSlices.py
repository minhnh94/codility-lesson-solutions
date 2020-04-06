def solution(m, a):
    count = 0
    for start in range(len(a)):
        count += 1
        if count >= 1000000000:
            return count
        end = start + 1
        while end < len(a) and len(set(a[start:end + 1])) == len(a[start:end + 1]):
            end += 1
            count += 1
            if count >= 1000000000:
                return count

    return count


print(solution(6, [3, 4, 5, 5, 2]))
