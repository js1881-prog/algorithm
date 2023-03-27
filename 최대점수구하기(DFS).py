import sys
sys.stdin = open("C:\\Study\\algorithm\\input.txt", "r")

def DFS(L, sum, time):
    global res
    if time>m:
        return
    if L==n:
        if sum > res:
            res = sum
    else:
        DFS(L+1, sum+pv[L], time+pt[L])
        DFS(L+1, sum, time)

if __name__ == "__main__":
    n, m = map(int, input().split())
    pv = list()
    pt = list()
    for i in range(n):
        a, b = map(int, input().split())
        pv.append(a)
        pt.append(b)
    res = -2147000000
    DFS(0, 0, 0)
    print(res)





























# def DFS(L, sum, time):
#     global res
#     print(L, sum, time)
#     if res[0] <= time <= m:
#         if res[1] < sum:
#             res[0] = time
#             res[1] = sum
#     for i in range(1, n+1):
#         if time > m:
#             break
#         if ch[i] == 0:
#             ch[i] = 1
#             DFS(L+1, sum+ls[i-1][0], time+ls[i-1][1])
#             ch[i] = 0


# if __name__ == "__main__":
#     n, m = map(int, input().split())
#     ls = []
#     ch = [0] * (n+1)
#     res = [0] * 2
#     for i in range(n):
#         a, b = map(int, input().split())
#         ls.append([a, b])
#     DFS(0, 0, 0)
#     print(res[1])
