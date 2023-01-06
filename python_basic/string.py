msg = "It is Time"
tmp = msg.upper()
print(tmp.find("T")) # find() => 인덱스 번호를 추출
print(tmp.count("T")) # 2 , "T" 가 몇개가 있냐

msg = "It is 1Time"
for i in range(len(msg)):
    print(msg[i], end=' ')
print()

for x in msg:
    print(x, end=' ')
print()

for x in msg:
    if x.isupper():
        print(x, end=' ')
print()

for x in msg:
    if x.islower():
        print(x, end=' ')
print()

for x in msg:
    if x.isalpha():
        print(x, end=' ')

tmp="AZ"
for x in tmp:
    print(ord(x)) # ord = 아스키 넘버를 출력 , A(65) ~ Z(90)

tmp2="az"
for x in tmp2:
    print(ord(x)) # ord = 아스키 넘버를 출력 , a(97) ~ z(122)

tmp3=65
print(chr(tmp3)) # chr = 아스키 넘버를 대응하는 문자로 출력 => A 출력

tmp4=66
print(chr(tmp4)) # B 출력
