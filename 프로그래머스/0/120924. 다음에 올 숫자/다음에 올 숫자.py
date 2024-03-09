def solution(common):
    if len(set([common[i]-common[i-1] for i in range(1, len(common))])) == 1:
        return 2 * common[-1] - common[-2]
    else:
        return common[-1] * (common[-1]//common[-2])
           
           