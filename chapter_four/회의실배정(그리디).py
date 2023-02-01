import sys

sys.stdin = open("C:\\Study\\algorithm\\input.txt", "r")

n = int(input())
meeting = []

for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))

meeting.sort(key=lambda x : (x[1], x[0])) # 튜플 자료형인 meeting의 1번과 0번이 역순으로 정렬

cnt = 1
end = meeting[0][1]

for i in range(1, n):
    if (end <= meeting[i][0]):
        end = meeting[i][1]
        cnt += 1

print(cnt)

