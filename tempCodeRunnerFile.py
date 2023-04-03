arr = [1,1,3,3,0,1,1]
p1=0
p2=1

def solution(arr):
    global p1,p2
    while(True):
        if p2 >= len(arr):
            return arr
        if arr[p1]==arr[p2]:
            arr.pop(p1)
        else:
            p1 += 1
            p2 += 1

print(solution(arr))
