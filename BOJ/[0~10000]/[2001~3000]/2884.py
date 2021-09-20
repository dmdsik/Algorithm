'''
현재 정해놓은 시간이 있다.
그 시간에 -45분을 해야 원하는 알람시간이 됩니다.

x시 45분 이상이면 x시
x시 44분 이하이면 x-1시 y+15분
else:
    


24:00

'''


hour, min = map(int,input().split())

if min >= 45:
    print(hour, min-45)
elif hour>0 and min < 45:
    print(hour-1, min+15)
else:
    print(23, min+15)


