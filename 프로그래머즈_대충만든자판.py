keymap = ["AGZ", "BSSS"]
targets = ["ASA","BGZ"]

def solution(keymap, targets):
    answer = []
    for target in targets:
        count, isTrue = 0, True
        for key in target:
            min_index = min([101] + [k.find(key)+1 for k in keymap if k.find(key)+1 != 0])
            if min_index == 101:
                isTrue = False
                break
            count += min_index
        # isTrue가 참이면 count 값을 추가하고 아니면 -1을 추가
        answer.append(count if isTrue else -1)
    return answer

# a = [k.find("A") for k in keymap]
# print(a)



    




