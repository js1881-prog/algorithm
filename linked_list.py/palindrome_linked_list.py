import collections
from typing import *

# 입력 1->2
# 출력 False    

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(self, head: ListNode) -> bool:
    q: List = []

    if not head:
        return True

    node= head
    # 리스트 변환
    while node is not None:
        q.append(node.val)
        node = node.next

    # 팰린드롬 판별
    while len(q) > 1:
        if q.pop(0) != q.pop(): # pop(0) = 첫번째 pop() = 마지막
            return False

    return True

# Deque를 이용한 최적화
def isPalindromeWithDeque(self, head: ListNode) -> bool:
    # 데크 자료형 선언
    q: Deque = collections.deque()

    if not head:
        return True
    
    node = head
    while node is not None:
        q.append(node.val)
        node = node.next
    
    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
    
    return True

# Runner를 이용한 기법
def isPalindromeWithRunner(self, head: ListNode) -> bool:
    rev = None
    slow = fast = head
    # 런너를 이용해 역순 연결 리스트 구성
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next
    
    # 팰린드롬 여부 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev


node1 = ListNode(1)
node2 = ListNode(2)
node3 = node2
node4 = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None

print(node1.val)
print(node2.val)
print(node3.val)
print(node4.val)

isPalindrome(Self, node1)
isPalindromeWithDeque(Self, node1) # Deque는 동적 배열을 꺼내올떄(pop(0) => 한칸씩 이동) 시프팅 되지 않기때문에 최적화가 가능하다.
isPalindromeWithRunner(Self, node1)
isPalindromeWithRunner(Self, node1)