import collections
import re
from typing import *

# 펠린드롬(palindrome) = 앞,뒤가 똑같은 단어나 문장으로, 뒤짚어도 같은 말이 되는 단어 또는 문장
# 문제는 대, 소문자 구분 X

s = "A man, a plan, a canal: Panama"

strs = []
for char in s:
    if char.isalnum(): # isalnum() = 영문자,숫자 여부를 판별하는 함수 => 영문자,숫자만 추가 가능
        strs.append(char.lower())
strs # ['a', 'm', 'a', 'n', 'a', 'p', 'l', 'a', 'n', 'a', 'c', 'a', 'n', 'a', 'l', 'p', 'a', 'n', 'a', 'm', 'a']

# while len(strs) > 1:
#     if strs.pop(0) != strs.pop(): # pop() 함수는 인덱스를 지정 가능, 0을 지정하면 맨 앞의 값을 가져올 수 있다.
#         # 맨 뒷부분의 pop()의 결과와 매칭해 나가면서 일치하지 않는 경우 False를 리턴
#         return False

def isPalindrome(self, s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False;
    return True;

# Deque를 이용한 최적화
# 덱(Deque)이란?
# Double-ended Queue의 약자로 양쪽 끝에서 삽입과 삭제가 모두 가능한 자료구조이다. 큐와 스택을 합친 형태로 생각할 수 있다.
def isPalindromeWithDeque(self, s: str) -> bool:
    # 자료형 데크로 선언
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())
    
    while len(strs) > 1:
        if strs.popleft() != strs.pop(): # stack의 pop()과 차이를 두기 위해서 왼쪽으로 빼낸다는 의미인 popleft()를 사용.
            return False;

    return True;

# 슬라이싱을 이용한 문제 풀이
def isPalindromeWithSlicing(self, s: str) -> bool:
    s = s.lower()
    # 정규식으로 불필요한 문자 필터링
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1] # 슬라이싱
# [::-1] 을 이용한 reverse