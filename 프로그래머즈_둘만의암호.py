from string import ascii_lowercase

def solution(s, skip, index):
    al = list(ascii_lowercase)
    result = ''
    
    for x in skip:
        al.remove(x)
    
    for c in s:
        result += al[(al.index(c) + index) % len(al)]
    return result


s = "aukks"
skip = "wbqd"
index = 5

print(solution(s, skip, index))

