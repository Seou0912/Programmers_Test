def solution(babbling):
    count = 0
    valid_sounds = ["aya", "ye", "woo", "ma"]

    for word in babbling:
        # 발음이 유효한지 확인하기 위한 임시 변수
        is_valid = True
        prev_sound = None  # 이전에 사용된 발음을 추적
        
        # 발음을 순서대로 체크하기 위해 임시 단어 변수 사용
        temp_word = word
        
        while temp_word:
            matched = False  # 현재 반복에서 매칭되는 발음이 있는지 확인
            
            for sound in valid_sounds:
                if temp_word.startswith(sound):
                    # 동일한 발음이 연속해서 사용되지 않았는지 확인
                    if sound == prev_sound:
                        is_valid = False
                        break
                    # 발음이 매치되면, 해당 발음을 제거하고 다음 발음 검사로 넘어감
                    temp_word = temp_word[len(sound):]
                    prev_sound = sound  # 이전 발음 업데이트
                    matched = True
                    break
            
            # 매치되는 발음이 없으면 루프 종료
            if not matched:
                break
        
        # 모든 발음이 조건에 맞게 사용되었고, temp_word가 완전히 소진되었다면 유효한 단어로 간주
        if is_valid and not temp_word:
            count += 1

    return count
