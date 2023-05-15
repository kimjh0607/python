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
b.remove(99.9)
print(b)
b.insert(0,'zero')
print(b)

x=[1,2,3,4]
y=['apple', 'banana']
z=x+y
z1=y+x
print(z)
print(z1)
x.extend(y)
print(x)

z=y*3
print(z)

q=['a', 'b', 'c']
w=[10, 11, q, True, 'string']
print(w[2][0:2])

#List Comprehension 리스트 내포
num = list(range(1,11))
print(num)
lst = [i**2 for i in num]
print(lst)
lst2 = ['even' if i%2==0 else 'odd' for i in num]
print(lst2)
lst3 = [i**2 for i in range(10) if i%2==0]
print(lst3)
