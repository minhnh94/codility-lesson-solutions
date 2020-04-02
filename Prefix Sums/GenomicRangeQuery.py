def solution(s, p, q):
    # 'A': 1, 'C': 2, 'G': 3, 'T': 4
    n = len(s)
    # index 0 means empty string
    all_letter_counts = {'A': [0] * (n + 1), 'C': [0] * (n + 1), 'G': [0] * (n + 1), 'T': [0] * (n + 1)}

    # Initialization
    for index, letter in enumerate(s):
        for def_letter in all_letter_counts.keys():
            single_letter_counts = all_letter_counts[def_letter]
            if letter == def_letter:
                single_letter_counts[index + 1] = single_letter_counts[index] + 1
            else:
                single_letter_counts[index + 1] = single_letter_counts[index]

            all_letter_counts[def_letter] = single_letter_counts

    # Calculation
    result_array = []
    for i in range(len(p)):
        num_A = all_letter_counts['A'][q[i] + 1] - all_letter_counts['A'][p[i]]
        num_C = all_letter_counts['C'][q[i] + 1] - all_letter_counts['C'][p[i]]
        num_G = all_letter_counts['G'][q[i] + 1] - all_letter_counts['G'][p[i]]
        # Turned out we don't even need T counts anw
        min_impact = 4
        if num_A > 0:
            min_impact = 1
        elif num_C > 0:
            min_impact = 2
        elif num_G > 0:
            min_impact = 3

        result_array.append(min_impact)

    return result_array
