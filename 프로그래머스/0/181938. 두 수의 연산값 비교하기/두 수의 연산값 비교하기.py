def solution (a, b):
    ab = int(str(a) + str(b))
    double_ab = 2 * a * b
    return ab if ab>= double_ab else double_ab
