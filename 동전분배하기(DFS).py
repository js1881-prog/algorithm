import sys
sys.stdin = open("C:\\Study\\algorithm\\input.txt", "r")

def DFS(L):
    global res, m, b
    if L==n:
        b = max(res) - min(res)
        if b < m:
            if len(set(res)) == len(res):
                m = b
    else:
        for i in range(3):
            res[i] += c[L]
            DFS(L+1)
            res[i] -= c[L]

if __name__ == "__main__":
    n = int(input())
    c = []
    for i in range(n):
        c.append(int(input()))
    m = 2147000000
    b = 0
    res = [0] * 3
    DFS(0)
    print(m)

