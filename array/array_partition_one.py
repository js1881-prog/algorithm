from typing import *

nums = [1, 4, 3, 2]

def arrayPairSum(self, nums: List[int]) -> int:
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
        # 1 2 3 4 5 6 7 8 9 
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []
        
    return sum

arrayPairSum(Self, nums=nums)

# nums = [1, 2, 3, 4]
# nums = [1, 2]
# sum = 1
# pair = []
# pair = [3, 4]
# sum = 1 + 3
# sum = 4
# return 4

# pair = [1, 4]
# min(pair) => min에 array를 넣어도 계산해줌

bpair = [1, 4]
min(bpair)
type(bpair)

# 짝수 번쨰 값을 계산한것과 같다
def arrayPairSumWithEvenNumber(self, nums: List[int]) -> int:
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        # 짝수 번째 값의 합 계산
        if i % 2 == 0:
            print(i)
            sum += n

arrayPairSumWithEvenNumber(Self, nums)


nums = [1, 4, 3, 2]
# with slicing
def arrayPairSumWithSlicing(self, nums: List[int]) -> int:
    return sum(sorted(nums)[::2])
# 가장 빠르다

arrayPairSumWithSlicing(Self, nums)