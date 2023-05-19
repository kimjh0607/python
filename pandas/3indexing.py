import pandas as pd
import numpy as np

#df.loc[행 인덱싱값] / df.loc[행 인덱싱값, 열 인덱싱값]
df = pd.DataFrame(np.arange(10, 22).reshape(3, 4),
                  index=["a", "b", "c"],
                  columns=["A", "B", "C", "D"])
print(df)
print(df.loc["a"])
print(df.loc["b":"c"])
print(df["b":"c"])
print(df.loc[["b", "c"]])
print(df.A > 15)
print(df.loc[df.A > 15])
#iloc 순서를 표시하는 정수 인덱스만 
print(df.iloc[0, 1])
print(df.iloc[:2, 2])
print(df.iloc[2:3, 1:3])
df.iloc[-1] = df.iloc[-1] * 2
print(df)