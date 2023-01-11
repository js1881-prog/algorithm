n = int(input())
a = list(map(int, input().split()))
ave = round(sum(a)/n) # round()소수 첫째 자리에서 반올림
min = 2147000000

for idx, x in enumerate(a): 
    tmp = abs(x - ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1 # 0번 인덱스 부터 시작, 학생번호
    elif tmp==min:
        if x > score:
            score = x
            res = idx + 1

print(ave, res)
        
    
    
        


