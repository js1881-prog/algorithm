import sys
sys.stdin = open("C:\\Study\\algorithm\\input.txt", "r")

def DFS(L,sum):
    global cnt
    if L==k:
        if sum==T:
            cnt += 1
    else:
        for i in range(cn[L]+1):
            DFS(L+1, sum+(cv[L] * i))

if __name__ == "__main__":
    T = int(input())
    k = int(input())
    cv = list()
    cn = list()
    for i in range(k):
        a, b = map(int, input().split())
        cv.append(a)
        cn.append(b)
    print(cv)
    print(cn)
    cnt = 0
    DFS(0, 0)
    print(cnt)
    
