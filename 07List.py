#리스트
a = []
a = ["Apple", 10, False]
a[2] = "test"
print(a)
print(a[2])

#List slicing
a = [1,10,11,20,21,30,31]
x = a[1:3]
print(x)
x1 = a[:3]
print(x1)
x2 = a[4:]
print(x2)
x3 = a[::2] #첫자리찍고 다다음
print(x3)
x4 = a[1::2]
print(x4)
x5 = a[::-1]
print(x5)

b = ["banana", "drum", True]
b.append(99.9)
b[1] = 44
del b[2]
print(b)

