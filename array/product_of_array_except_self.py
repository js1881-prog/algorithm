from typing import *

nums = [1, 2, 3, 4]

def productExceptSelf(self, nums: List[int]) -> int:
    out = []
    p = 1
    # 왼쪽 곱셈
    for i in range(0, len(nums)):
        out.append(p)
        p = p * nums[i]
        print(out)
    p = 1
    # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    for i in range(len(nums) - 1, - 1, - 1):
        print("i=", i)
        out[i] = out[i] * p
        print("out=",out)
        print("nums[i]", i)
        p = p * nums[i]
        print("p=", p)
    return out

productExceptSelf(Self, nums)




range_test_list = [11, 22, 33, 44, 55]
for i in range(len(range_test_list) - 1, - 1, - 1):
    print(i) # 4 3 2 1 0 
