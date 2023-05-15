#builtins 함수
help(len)
dataset = list(range(1,6))
print(dataset)
print(len(dataset))
print(sum(dataset))
print(max(dataset))
print(min(dataset))

#import 함수
import statistics
from statistics import variance, stdev

print('평균 : ', statistics.mean(dataset))
print('중위수 : ', statistics.median(dataset))
print('표준분산 : ', variance(dataset))
print('표본 표준편차 : ', stdev(dataset))

import builtins
print(dir(builtins))

#import예시1
#from lib11.math_test import pytha
#pytha(3,4)

#import예시2
import lib11.math_test
lib11.math_test.pytha(3,4)
