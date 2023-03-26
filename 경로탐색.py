import sys
sys.stdin = open("C:\\Study\\algorithm\\input.txt", "r")

# 1. ch[] 를 이용해 중복된 for문의 i를 가지 않도록 체크
# 2. DFS(V) == for문의 i 중복이면 return
# 3. DFS(V) == 5 면 출력
# 4. DFS(V) == for문의 i
# 5. 1,2 조건을 만족할때 인접행렬을 조사하여 i의 값이 합당한지 판별
def DFS(V, s):
    return


if __name__ == "__main__":
    n, m = map(int, input().split())
    ls = [[0] * (n) for _ in range(n)]
    ch = [0] * n
    for i in range(m):
        a, b = map(int, input().split())
        ls[a-1][b-1] = 1

print(n, m)

for x in ls:
    print(x, end= ' ')
    print()


