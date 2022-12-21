from typing import *
import re
import collections

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
    .lower().split()
        if word not in banned]
    print(words)
    
    counts = collections.Counter(words) # Counter({5: 3, 6: 2, 1: 1, 2: 1, 3: 1, 4: 1}), 키에는 아이템의 값이, 값에는 해당 아이템의 갯수가 들어간다.
    print(counts)
    return counts.most_common(1)[0][0]

print(mostCommonWord(Self, paragraph=paragraph, banned=banned));

