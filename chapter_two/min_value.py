arr = [5, 3, 7, 9, 2, 5, 2, 6]
arrMin = float('inf') # float에서 가장 큰값이 저장된다, 가장 큰 값으로 초기화
for i in range(len(arr)):
    if arr[i]<arrMin:
        arrMin=arr[i] 