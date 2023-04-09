import sys
sys.stdin = open("C:\\Study\\algorithm\\input.txt", "r")

def DFS(L, P):
    global cnt
    if L==n:
        cnt += 1
        for j in range(P):
            # chr => 숫자를 문자로 chr[65] = 'A'(대문자 A) 따라서 64를 더해주면
            # 1이면은 A, 2 = B, 3 = C, 4 = D
            print(chr(res[j]+64), end='')
        print()
    else:
        for i in range(1, 27):
            if i == code[L]:
                res[P] = i
                DFS(L+1, P+1)
            elif i >= 10 and code[L] == i//10 and code[L+1] == i%10:
                res[P] = i
                DFS(L+2, P+1)

if __name__ == "__main__":
    code = list(map(int, input()))
    n = len(code)
    code.insert(n, -1)
    res = [0] * (n+3)
    cnt = 0
    DFS(0, 0)
    print(cnt)