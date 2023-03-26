import sys
sys.stdin = open("C:\\Study\\algorithm\\input.txt", "r")

if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [[0] * (n) for _ in range(n)]
    for i in range(m):
        a, b, c = map(int, input().split())
        res[a-1][b-1] = c

    for x in res:
        for j in x:
            print(j, end=' ')
        print()