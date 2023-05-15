#Tuple 튜플 - immutable 배열같은건가?
#인덱싱과 슬라이싱 등의 작업가능 for문 이용가능
#튜플의 요소를 직접 변경하는 것은 불가능 
t = ('apple', 10, True)
print(t)
t1 = (100)
print(t1, type(t1))
t2 = (100,)
print(t2, type(t2))

print(t[1], t[1:3], t[-1])

print(t+t2)
print(t*3)

city,town = ("seoul", "Guro")
print(city, town)

my_tuple = (1, "apple", 3.14)
print(my_tuple)

my_tuple2 = 1, "apple", 3.14
print(my_tuple2)