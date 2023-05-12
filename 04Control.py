#제어문

#조건문
# score = int(input('점수 입력 : '))
# grade = ''
# if score<=100 and score>=85:
#     grade = '우수'
# elif score>=70:
#     grade = '보통'
# else:
#     grade = '부족'
# print('당신의 점수 : %d / 등급 : %s' %(score,grade))

# num=2
# result=0
# if(num>6): 
#     result = num*2
# else: 
#     result = num+2
# print(result)

#삼항연산자
# print(num*2 if num>6 else num+2) 


#while문
cnt=tot=0
datalst=[]
while cnt<5:
    cnt+=1
    tot+=cnt
    datalst.append(cnt)
    print(cnt,tot)
print(datalst)

#4의 배수의 합
int=sum=0
while int<=100:
    int+=1
    if (int%4==0):
        sum+=int
    
print('%d' %(sum))

i=0
while i<10:
    i+=1
    if i==3:
        continue
    if i==6:
        break
    print(i,end=' ') #end를 붙이면 println같은 효과
print()

#반복문
#for문
string='abcdefghijklmn'
print(len(string))
for s in string:
    print(s)
print()

lst = [1,2,3,4,5,6,7]
for e in lst:
    print(e,end=' ')
print()

print(range(10))
for e in range(10):
    print(e,end=' ')
print()

for e in range(3,10):
    print(e,end=' ')
print()

for e in range(0,10,4):
    print(e,end=' ')
print()

lst=['A','B','C']
if 'D' in lst:
    print("Ok")
else:
    print('No')

