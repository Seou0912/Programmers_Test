def solution(keymap, targets):
    answer = []
    key_dict = {}
    
    # Create a dictionary with the character as the key and the minimum key press count as the value
    for i, keys in enumerate(keymap):
        for j, char in enumerate(keys):
            if char in key_dict:
                key_dict[char] = min(key_dict[char], j+1)
            else:
                key_dict[char] = j + 1
                
    # Calculate the minimum key press count for each target
    for target in targets:
        press_count = 0
        for char in target:
            if char not in key_dict:
                press_count = -1
                break
            press_count += key_dict[char]
        answer.append(press_count)
        
    return answer
