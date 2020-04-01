def solution(x, a):
    positions = set(list(range(1, x + 1)))
    for index, position in enumerate(a):
        positions.discard(position)
        if len(positions) == 0:
            return index

    return -1
