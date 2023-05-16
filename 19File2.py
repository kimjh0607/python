import pandas as pd #별칭
import os

os.chdir('D:/모음/python/pythonwork/data')

iris = pd.read_csv('iris.csv')
print(iris.info())

st=pd.read_csv('student.csv', header=None)
print(st)
col_names = ['no', 'name', 'height', 'weight']
st.columns = col_names
print(st)

BMI = st['weight']/(st['height']*0.01)**2
print(BMI)

st['BMI']=BMI.round(2)
print(st)


labels=[]
for i in st.BMI:
    if i>=18 and i<=23:
        labels.append("정상")
    elif i>23:
        labels.append("비만")
    else:
        labels.append("저체중")
st['labels']=labels
print(st)

st.to_csv('st_info.csv', index=None, encoding='utf-8')

st=pd.read_csv('st_info.csv', encoding='utf-8')
print(st)

sam=pd.ExcelFile('sam_kospi.xlsx')
kospi=sam.parse("sam_kospi")
print(kospi.info())
high = kospi['High']
low = kospi['Low']

print('High mean', high.mean())
print("Low mean", low.mean())