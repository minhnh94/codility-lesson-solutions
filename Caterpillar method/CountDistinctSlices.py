def solution(m, a):
    visited = [False] * (m + 1)
    start = end = 0
    count = 0
    while start < len(a):
        if end < len(a) and visited[a[end]] is False:
            visited[a[end]] = True
            end += 1
        else:
            count += end - start
            if count >= 1000000000:
                return 1000000000
            visited[a[start]] = False
            start += 1

    return count
