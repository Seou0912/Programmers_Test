def solution(chicken):
    free_chicken = 0
    coupons = chicken

    while coupons >= 10:
        free_chicken += coupons // 10
        coupons = coupons // 10 + coupons % 10

    return free_chicken