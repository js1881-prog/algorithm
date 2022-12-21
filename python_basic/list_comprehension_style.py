import re

str1 = 'Hello World';

# re.findall(r'패턴 문자열', '문자열')
str1s = [
    str1[i: i + 2].lower() for i in range(len(str1) -1)
    if re.findall('[a-z]{2}', str1[i: i + 2].lower())
]

str1s
