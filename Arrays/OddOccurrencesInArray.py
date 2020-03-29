from collections import Counter


def solution(a):
    count_dict = Counter(a)
    return sum([key for key, freq in count_dict.items() if freq % 2 != 0])
