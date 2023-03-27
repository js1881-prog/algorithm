import sys
sys.stdin = open("C:\\Study\\algorithm\\input.txt", "r")

# 1. ch[] 를 이용해 중복된 for문의 i를 가지 않도록 체크
# 2. DFS(V) == for문의 i 중복이면 return
# 3. DFS(V) == 5 면 출력
# 4. DFS(V) == for문의 i
# 5. 1,2 조건을 만족할때 인접행렬을 조사하여 i의 값이 합당한지 판별
def DFS(v):
    global cnt
    if v==n:
        print(path)
        cnt += 1
    else:
        for i in range(1, n+1):
            if ls[v][i] == 1 and ch[i] == 0:
                ch[i] = 1
                path.append(i)
                DFS(i)
                path.pop()
                ch[i] = 0

if __name__ == "__main__":
    n, m = map(int, input().split())
    ls = [[0] * (n+1) for _ in range(n+1)]
    ch = [0] * (n+1)
    cnt = 0
    for i in range(m):
        a, b = map(int, input().split())
        ls[a][b] = 1
    ch[1] = 1
    path = []
    path.append(1)
    DFS(1)
    print(cnt)

# print(n, m)

# for x in ls:
#     print(x, end= ' ')
#     print()


