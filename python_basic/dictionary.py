import collections

a = dict()
a = {} # dict()를 간단하게 선언
a = {'key1' : 'value1', 'key2' : 'value2'}
a # {'key1' : 'value1', 'key2' : 'value2'}
a['key3'] = 'value3'
a # {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3'}
a['key1'] # 'value1'

try:
    print(a['key4'])
except KeyError:
    print('존재하지 않는 키') # try 예외 처리

# 딕셔너리의 items() 메소드를 사용하면 for 반복문으로 딕셔너리의 키/값 을 조회 가능.
for k,v in a.items():
    print(k,v)
# key1 value1
# key2 value2
# key3 value3

del a['key1'] # 삭제
a # {'key2': 'value2', 'key3': 'value3'}

# defaultdict 객체 => 존재하지 않는 키를 조회 할 경우 디폴트 값을 기준으로 해당 키에 대한 딕셔너리 아이템을 생성해준다.
# collections.defaultdict 클래스를 가진다.
c = collections.defaultdict(int)
c['A'] = 5
c['B'] = 4 
c # defaultdict(<class 'int'>, {'A' : 5, 'B' : 4})
c['C'] += 1 # defaultdict의 default 0을 기준으로 자동으로 생성한 후 여기에 1을 더해 최종적으로 1이 생성된다.
c # defaultdict(<class 'int'>, {'A': 5, 'B': 4, 'C': 1})

# Counter = 아이템에 대한 갯수를 계산해 딕셔너리로 리턴
a = [1, 2, 3, 4, 5, 5, 5, 6, 6]
b = collections.Counter(a)
b # Counter({5: 3, 6: 2, 1: 1, 2: 1, 3: 1, 4: 1}), 키에는 아이템의 값이, 값에는 해당 아이템의 갯수가 들어간다.
# 그 후에 딕셔너리를 한 번 더 래핑하는 collections.Counter 클래스를 가진다.
type(b) # <class 'collections.Counter'>

# Counter 객체에서 가장 빈도 수가 높은 요소
b.most_common(2) # [(5, 3), (6, 2)], 가장 빈도수가 높은 요소 2개를 추출

# 입력 순서가 유지되는 OrderedDict
collections.OrderedDict({'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}) # OrderedDict([('banana', 3), ('apple', 4), ('pear', 1), ('orange', 2)])
