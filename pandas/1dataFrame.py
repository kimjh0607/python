import pandas as pd
import numpy as np
'''
Pandas.DataFrame 클래스 구조

DataFrame 클래스 - 2차원 행열 데이터에 인덱스를 붙인 것과 유사
pandas.DataFrame으로 생성된 인스턴스는 크기의 변경이 가능한 2차원 배열 (Series는 1차원)
데이터 구조에는 레이블이 지정된 축인 행과 열까지 포함되며, 클래스 매서드를 통해 레이블의 수정이 가능
2차원이므로 row index와 column index
공통 인덱스를 가지는 열 시리즈(column series)를 딕셔너리로 묶어놓은 것

class pandas.DataFrame(data=None, index=None, columns=None, copy=None)

Parameter
data : ndarray, Iterable, dict, DataFrame
dict에는 Series, 배열 등등 list와 유사한 오브젝트 가능
데이터가 dict인 경우 열(Columns)의 순서는 삽입 순서에 따라

index : 인덱스 또는 배열형태의 객체
인스턴스에 설정되는 행 레이블입니다. 입력하지 않으면 기본 인덱스가 설정 (0, 1, 2, 3...)
columns : 인덱스 또는 배열형태의 객체
인스턴스에 설정되는 열 레이블입니다. 입력하지 않으면 기본 인덱스가 설정 (0, 1, 2, 3...)
dtype : dtype 데이터 유형을 강제하고자 할 때 값 기본값은 None이며 None일경우 type이 자동 추론

copy : bool
Ture 일 경우 원본 데이터를 수정하더라도 인스턴스가 변경되지 않음
False일 경우 원본데이터를 수정할 시 인스턴스의 값도 변경
'''
 # 2*2 짜리 random array 생성
np.random.seed(0)
arr = np.random.randint(10, size=(2, 2)) 
print(arr)

dfa=pd.DataFrame(arr,copy=False)
dfb=pd.DataFrame(arr,copy=True)
arr[0,0]=100
print(dfa)
print(dfb)

print("=== dictionary로 생성 ==========")
data = {
    "2015": [9904312, 3448737, 2890451, 2466052],
    "2010": [9631482, 3393191, 2632035, 2431774],
    "2005": [9762546, 3512547, 2517680, 2456016],
    "2000": [9853972, 3655437, 2466338, 2473990],
    "지역": ["수도권", "경상권", "수도권", "경상권"],
    "2010-2015 증가율": [0.0283, 0.0163, 0.0982, 0.0141]
}
dfc=pd.DataFrame(data=data)
print(dfc)
print("=== index columns 설정 ==========")
columns = ["지역","2015","2010","2005","2000","2010-2015 증가율"]
index = ["서울", "부산", "인천", "대구"]
df = pd.DataFrame(data, index=index, columns=columns)
print(df)
print(df.values)
print(df.columns,"\n",df.index)
df.index.name="city"
df.columns.name = "year"
print(df)
print("==== axis change =================================")
print(df.T)
print("==== data update =================================")
df["2010-2015 증가율"] = df["2010-2015 증가율"] * 100
print(df)
print("==== data insert =================================")
df["2005-2010 증가율"] = ((df["2010"] - df["2005"]) / df["2005"] * 100).round(2)
print(df)
print("==== data delete =================================")
del df["2010-2015 증가율"]
print(df)
#column indexing
print( df["지역"] )
print( df[["2010","2015"]] )
print( type(df[["2010"]]) )
print( type(df["2010"]) )
#print( df[0]) #key error
df2 = pd.DataFrame(np.arange(12).reshape(3,4))
print( df2 )
print( df2[2])
print( df2[[1,2]])
#row indexing(slicing 필수)
print( df[:2])
print( df["서울":"부산"] )
#individual data indexing
print( df["2015"]["서울"] )