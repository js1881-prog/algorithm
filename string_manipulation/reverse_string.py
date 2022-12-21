from typing import *

s = ["h", "e", "l", "l", "o"]
s2 = ["H", "a", "n", "n", "a", "h"]

def reverseString(self, s:List[str]) -> None:
    left = right = 0
    len(s) - 1
    while left < right:
        print(s[left]), print(s[right])
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    
reverseString(Self, s);

def reverseStringWithReserveMethod(self, s: List[str]) -> List[str]:
    s.reverse();
    return s

reverseStringWithReserveMethod(Self, s);
s

