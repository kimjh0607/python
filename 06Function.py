#함수
def print_max(a,b):
    if a>b:
        print(a, 'is bigger than' , b)
    elif a==b:
        print(a, 'is equal to' , b)
    else:
        print(b, 'is bigger than' , a)
print_max(5,7)

def mul(a,b=1):
    c=a*b
    return(c)
print(mul(3,7))
print(mul(2))

#전역 및 지역변수
x=100
def func(x):
    print(x)
    x=2
    print(x)
func(x)

def func2():
    global x
    print(x)
    x=2
    print(x)
func2()

def f(i,lst):
    i+=1
    print(i)
    lst.append(0)
k = 100
m = [1,2,3]
f(k,m)
print(k,m)

def reprint(a,b,c):
    print(a+1, b*2, c/2)
reprint(6, 4, 16)
reprint(c=16, a=6, b=4)

def sum(*numbers):
    tot = 0
    for num in numbers:
        tot += num
    return tot

print(sum(1,2,3,4,5,6,7,8,9,10))

def sum2(*numbers):
    count = 0
    tot = 0
    for num in numbers:
        count+=1
        tot+=num
    return count,tot
count, sum = sum2(1, 3, 4, 5, 6, 7, 45, 3)
print(count, sum)
