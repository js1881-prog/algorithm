n = 8
m = 4
section = [2, 3, 6]

def solution(n, m, section):
    paint, answer = section[0]-1, 0
    for v in section:
        if paint < v:
            paint = v+m-1
            answer += 1
    
    return answer

print(solution(n, m, section))

        



solution(n, m, section)