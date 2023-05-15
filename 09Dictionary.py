# dictionary 자바에서 map
# 'key : value'의 쌍을 요소로 갖는 자료형. 
# 중괄호 {}를 사용하여 생성
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(my_dict['name'])  # 출력: John
my_dict['job'] = 'Engineer'  # 새로운 키-값 쌍 추가
my_dict['age'] = 31  # 기존 키의 값 변경
print(my_dict)


dic = dict(key1=10, key2=20, key3=30)
print(dic)
dic1 = {'name' : 'alex', 'age' : 10, 'gender' : 'man'}
print(dic1)
persons=[('a',10),('b',22),('c',33)]
perdic = dict(persons)
print(perdic)

print(dic['key1'])
dic1['name'] = 'mark'
print(dic1)
del perdic['b']
print(perdic)
perdic['d'] = 44
print(perdic)

for key in dic.keys():
    print(key)
for val in dic.values():
    print(val)
for i in dic.items():
    print(i)

charset = ['abc', 'code', 'rule', 'rule', 'adb']
wc={}
for key in charset:
    wc[key] = wc.get(key, 0) + 1
print(wc)
print(wc.get('kkkk', '키 없음'))
wc.update(persons)
print(wc)