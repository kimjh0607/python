'''
사용자에게 정수를 입력 받아 계속 더하다가 음수를
입력받으면 중단하고 계산 최종 결과값을 출력
input()
4
5
6
-4
15
'''

sum = 0
while True:
    num = int(input())
    if num < 0:
        
