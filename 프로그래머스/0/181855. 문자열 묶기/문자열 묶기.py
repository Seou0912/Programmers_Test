def solution(strArr):
    length_counts = {}
    for string in strArr:
        length = len(string)
        if length not in length_counts:
            length_counts[length] = 1
        else:
            length_counts[length] += 1
    return max(length_counts.values())