import sys
sys.stdin = open("C:\\Study\\algorithm\\input.txt", "r")
input = sys.stdin.readline
#s=input().rstrip() # readline 문자열 읽을때 줄바꿈 삭제시켜주는거 같이쓰자
def DFS(L):
    global cnt
    if L == m:
        for j in range(m):
            print(res[j], end=' ')
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            res[L] = i
            DFS(L+1)

if __name__ == "__main__" :
    n, m = map(int, input().split())
    res = [0] * m
    cnt = 0
    DFS(0)
    print(cnt)


