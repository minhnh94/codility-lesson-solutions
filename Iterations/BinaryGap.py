def solution(n):
    dec_n = bin(n)[2:]
    splited = dec_n.split('1')
    max_len = 0
    for index, substr in enumerate(splited):
        if index == len(splited) - 1 or substr == '':
            continue

        max_len = max(max_len, len(substr))

    return max_len
