import pandas as pd
'''
Series 클래스 - 1차원 배열과 유사
값/데이터(value)+인텍스(index)
'''
#생성
s = pd.Series([9509458,3350380,2948375,2385412])
print(s)
si = pd.Series([9509458,3350380,2948375,2385412],
              index=["서울","부산","인천","대구"])
si2 = pd.Series({"서울":9628458,"대전":2474612,"부산":3251380,"인천":3048245})
print(si)
print(si2)
print(s.index)
print(si.index)
print(si.values)
si.name="인구"
si2.name="population"
si.index.name = "도시"
si2.index.name = "city"
print(si,'\n',si2)
#연산
print(si/10000)
print(si//10000)
print(si+9999)
#값 읽기
print( si[1],si["부산"],si[3],si["대구"] )
print( si[[0,3,1]],si[["서울","인천","부산"]] )
print( si[(2500000<si)&(si<500e4)] )
print( si[1:3] )
print( si["부산":"대구"] )
s1 = pd.Series(range(3),index=["A","B","C"])
print(s1,s1.A,s1.B)
print("서울" in si,"울산" in si)
for k,v in si.items():
    print("%s=%d" % (k,v))
#인텍스별 연산
ds=si-si2
print(ds)
print(si.values-si2.values)
print(ds.notnull())
print(ds[ds.notnull()])
rs=(ds)/si2*100
rs=rs[rs.notnull()]
print(rs)
rs["부산"]=2.0
del rs["서울"]
print(rs)