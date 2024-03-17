def solution(quiz):
    result = []
    for equation in quiz:
        parts = equation.split()  # 수식을 연산자와 숫자로 나누기
        x, op, y, equal, z = parts  # 각 부분 변수에 할당
        if op == '+':  # 덧셈인 경우
            if int(x) + int(y) == int(z):  # 올바른 결과인지 확인
                result.append("O")
            else:
                result.append("X")
        elif op == '-':  # 뺄셈인 경우
            if int(x) - int(y) == int(z):  # 올바른 결과인지 확인
                result.append("O")
            else:
                result.append("X")
    return result