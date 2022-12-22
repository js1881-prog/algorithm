from typing import *

nums = [2, 7, 11, 15]   
target = 9

# 브루트 포스
# 효율적이지 못하다
# 시간복잡도 O(n제곱)
def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

# in을 이용한 탐색
# 파이썬 내부 함수 in을 사용해 빨라지긴 했지만 여전히 시간 복잡도는 O(n제곱)
def twoSumWithIn(self, nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]
# index = 배열에서 원하는 숫자의 값의 위치를 찾음 여기서 index(2)이면 0

def twoSumThird(self, nums: List[int], target: int) -> List[int]:
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i
    # nums_map = {2:0, 7:1, 11:2, 15:3}
    
    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]

# map 안의 key를 in으로 비교가능(int로)
map = {3:3, 4:2, 5:1}

if 3 in map:
    print("yes")

# 딕셔너리를 두개 사용한것을 하나의 for문으로 통합
def twoSumFourth(self, num: List[int], target: int) -> List[int]:
    nums_map = {}
    # 하나의 for 문으로 통합
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i

# 투 포인터를 이용한 방법,
# 양 끝에서 두 포인터가 시작해서 목표하는 result 값보다 더 크면 오른쪽 포인터를 왼쪽으로 이동하고,
# 값이 더 작으면 왼쪽 포인터를 오른쪽으로 이동한다
nums = [2, 7, 11, 15]   
def twoSumFifth(self, nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1
    while not left == right:
        # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]
twoSumFifth(Self, nums=nums, target=target)
# => 이 문제는 투 포인터로 풀 수 없다. 그렇다고 한다 제대로 풀려면 정렬이 필요한데 이러면 인덱스가 엉망이 되기 떄문
