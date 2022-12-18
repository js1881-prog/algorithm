import collections
import heapq
import functools
import itertools
import re
import sys
import math
import bisect
from typing import *
# 책에서 사용할 python 내부 라이브러리

numbers = []
for n in range(1, 10):
    numbers.append(n)
    print(n)

# [] 리스트 안에 .append 를 추가
[x for x in range(1, 10 + 1) if x % 2 == 0]
[n * 2 for n in range(1, 10 + 1) if n % 2 == 1]

# 딕셔너리 또한 컴프리헨션 가능
# a = {}
# for key, value in original.items():
#     a[key] = value

# a = {key: value for key, value in original.items()}