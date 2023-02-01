import sys
sys.stdin = open("C:\\Study\\algorithm\\input.txt", "r")

l = int(input())
storage_height = list(map(int, input().split()))
m = int(input())
storage_height.sort()

for i in range(m):
    storage_height[0] = storage_height[0] + 1
    storage_height[l-1] = storage_height[l-1] - 1
    storage_height.sort()

print(storage_height[l-1] - storage_height[0])

