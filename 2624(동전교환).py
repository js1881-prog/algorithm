import sys
sys.stdin = open("C:\\Study\\algorithm\\input.txt", "r")
input = sys.stdin.readline
#s=input().rstrip() # readline 문자열 읽을때 줄바꿈 삭제시켜주는거 같이쓰자

def DFS(L, sum):
    global res
    if L>res:
        return
    if sum > m:
        return
    if sum==m:
        if L < res:
            res = L
    else:
        for i in range(n):
            DFS(L+1, sum+a[i])

if __name__ == "__main__":
    n = int(input())
    a = list(map(int,input().split()))
    m = int(input())
    res = 2147000000
    a.sort(reverse=True)
    DFS(0, 0)
    print(res)


