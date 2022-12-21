from typing import *;

logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
# Desired result = ["let1 art can", "let2 own kit dig", "let3 art zero", "dig1 8 1 5 1", "dig2 3 6"]

def reorderLogFiles(self, logs: List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs: # 문자열.split() 함수는 문자열을 일정한 규칙으로 잘라서 리스트로 만들어 주는 함수입니다.
        if log.split()[1].isdigit():  # isdigit() => 숫자인지 문자인지 판별
            digits.append(log) # 숫자면 True => digit(숫자)에 추가.
        else:
            letters.append(log) # 문자면 False => letters(문자)에 추가

    # 2개의 키를 람다 표현식으로 정렬
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits