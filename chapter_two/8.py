from typing import *

def reverse(x):
    res=0
    while x>0:
        t=x%10
        res=res*10+t
        x=x//10
    return res

def isPrime(x):
    if x==1:
        return False
    for i in range(2, x//2 +1): # 소수가 아니면 해당 수로 나눠지는 수는 2를 제외한 그 수의 절반까지만 포함하면 셀수있다.
        if x%i==0:
            return False
    else:
        return True
    
n = int(input())
a = list(map(int, input().split()))

for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')


