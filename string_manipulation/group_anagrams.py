from typing import *
import collections

# 애너그램 => 일종의 언어유희로 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것

# - ''.join(리스트)
#  ''.join(리스트)를 이용하면 매개변수로 들어온 ['a', 'b', 'c'] 이런 식의 리스트를 'abc'의 문자열로 합쳐서 반환해주는 함수인 것입니다.
# - '구분자'.join(리스트)
# '구분자'.join(리스트)를 이용하면 리스트의 값과 값 사이에 '구분자'에 들어온 구분자를 넣어서 하나의 문자열로 합쳐줍니다.
# '_'.join(['a', 'b', 'c']) 라 하면 "a_b_c" 와 같은 형태로 문자열을 만들어서 반환해 줍니다.

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        # 정렬하여 딕셔너리에 추가
        print(anagrams[''.join(sorted(word))])
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())


groupAnagrams(Self, strs)


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagrams = collections.defaultdict(list)

for word in strs:
    # 정렬하여 딕셔너리에 추가
    anagrams[''.join(sorted(word))].append(word)
    print(anagrams)

# 1. "eat" => sorted => "aet" 에.append "eat"
# 2. "tea" => sorted => "aet" 에.append "tea"
# 3. "tan" => sorted => "ant" 에.append "tan"
# 4. "ate" => sorted => "aet" 에.append "ate"
# 5. "nat" => sorted => "ant" 에.append "nat"
# 6. "bat" => sorted => "abt" 에.append "bat"
# return list(angram.values()) => [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
