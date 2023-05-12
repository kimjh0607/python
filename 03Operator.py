#산술연산
num1 = 100
num2 = 20

print('add', num1+num2)
print('sub', num1-num2)
print('mul', num1*num2)
print('div', num1/num2)
print('rem', num1%num2)
print('quo', num1//num2)
print('squ', num1**num2)

#관계연산자, 논리연산자
print(num1>num2)
print(num1<num2)
print(num1>=num2)
print(num1<=num2)
print(num1==num2)
print(num1!=num2)
print(num1>=50 and num2<=10)
print(num1>=50 or num2<=10)
print(not(num1>=50))

#대입연산자
i = 10
print(i)
i = i + 1
print(i)
i += 1
print(i)
i *= 2
print(i)

i=j=100
print(i,j)
i,j=99,88
j,i=i,j
print(i,j)

lst=[1,2,3,4,5]
i,*j=lst
print(i,j)
*i,j=lst
print(i,j)

i,*j,k=lst
print(i,j,k)