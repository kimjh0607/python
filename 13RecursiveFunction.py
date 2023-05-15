def Counter(n):
    if n==0:
        return 0
    else:
        Counter(n-1)
        print(n,end=' ')
Counter(10)