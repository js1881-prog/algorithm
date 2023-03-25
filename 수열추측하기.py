import sys
sys.stdin = open("C:\\Study\\algorithm\\input.txt", "r")

def DFS(L):
    if L==n:
        res = 0
        for i in range(n):
            res += b[i] * p[i]
        if res == f:
            print(p)
            for y in p:
                print(y, end=' ')
            sys.exit(0)

    for i in range(1, n+1):
        if ch[i] != 1:
            ch[i] = 1
            p[L] = i
            DFS(L+1)
            ch[i] = 0    

if __name__ == "__main__":
    n, f = map(int, input().split())
    b = [1] * n
    p = [0] * n
    ch = [0] * (n+1)
    for i in range(1, n):
        b[i] = b[i-1] * (n-i) // i
    DFS(0)
        


