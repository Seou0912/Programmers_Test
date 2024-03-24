def solution(name, yearning, photo):
    # 그리움 점수를 저장할 딕셔너리 생성
    yearning_dict = {name[i]: yearning[i] for i in range(len(name))}
    result = []

    # 각 사진에 대한 추억 점수 계산
    for i in range(len(photo)):
        score = 0  # 각 사진의 추억 점수 초기화
        for person in photo[i]:
            # 사진 속 인물의 그리움 점수를 더함
            if person in yearning_dict:
                score += yearning_dict[person]
        result.append(score)  # 계산된 추억 점수를 결과 배열에 추가

    return result
