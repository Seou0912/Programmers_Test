def solution(hp):
    gen= hp // 5
    hp %= 5
    sol = hp //3
    hp %= 3
    ant = hp
    return gen + sol + ant