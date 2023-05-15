#Set
st = {1,1,2,2,2,2,2,3,3,3,3,4,4,4,4,45,5,5,4}
print(st)

mylist = ['A', 'A', 'A', 'B', 'b', 'b', 'C']
st1 = set(mylist)
print(st1)

st.add(7)
print(st)
st.update({5, 8, 9, 23, 22})
print(st)
st.remove(2)
print(st)
st.clear()
print(st)

#집합연산
a = {10, 30, 50, 70}
b = {10, 20, 50, 90}

#교집합 {10,50}
#i = a&b
i=a.intersection(b)
print(i)

#합집합
#u = a|b
u=a.union(b)
print(u)

#차집합
#d = a-b
d=a.difference(b)
print(d)