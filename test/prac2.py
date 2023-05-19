'''
윤년 확인
1 연도를 4로 균등하게 나눌 수 있는 경우 2단계로 이동
그렇지 않으면 5단계로 이동
2 연도를 100으로 균등하게 나눌 수 있는 경우 3단계로 이동
그렇지 않으면 4단계로 이동
3 연도를 400으로 균등하게 나눌 수 있는 경우 4단계로 이동
그렇지 않으면 5단계로 이동
4 해당 연도는 윤년(366일)
'''

from tools import is_leap_year

while True:
    year = int(input())
    if year == 0:
        break
    if is_leap_year(year):
        print(f"{year} 윤년임")
    else is_leap_year(year):
        print(f"{year} 윤년아님")