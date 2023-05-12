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
