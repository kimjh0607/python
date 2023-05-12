float('1.234')
string = 'abc'
try:
    float(string)
except:
    print('fail to convert ',end='')
    print(string)
else:
    print('ok')
finally:
    print('finally')