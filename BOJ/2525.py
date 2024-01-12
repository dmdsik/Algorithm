'''
A, B = map(int, input().split())
C = int(input())

A += t // 60
B += t % 60

if m >= 60:
 h += 1
 m -= 60
elif h >= 24:
 h -= 24

print(h, m)

전제가 틀렸어 안맞아...
예시로 주어진 값은 맞지만 모든 인풋에 대응하지 않음 -> 쓰레기
'''

# B와 C를 더했을때 60이 넘으면, 그것을 60으로 나눈 후 몫을 A에 더해야 함
# 따라서 "B + C >= 60"인 조건으로 분류 해야함
# A, B, C외에 B + C를 더한 후 나온 몫과 나머지를 담는 변수도 하나 만들어서 관리하는게 나을듯?

A, B = map(int, input().split())
C = int(input())

hour = (B+C) // 60
min = (B+C) % 60

if(B+C >= 60):
 if(A+hour) >= 24:
  A -= 24
 A += hour
 print(A, min)

else:
 if(A >= 24):
  A -= 24
 print(A, B+C)
