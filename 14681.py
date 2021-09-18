

#입력 받을때 map()을 이용
#파이썬은 항상 자료형을 초기화 시켜주어야 합니다.
'''
이 방식의 입력이 아래의 입력 방식과 어떻게 다른지
런타임 에레가 뜹니다.
x, y = input().split()
x = int(x)
y = int(y)
'''
x = int(input())
y = int(input())

'''
++ == 1
-+ == 2
-- == 3
+- == 4
'''

if x>0 and y>0:
    print(1)

elif x<0 and y>0:
    print(2)

elif x<0 and y<0:
    print(3)

else:
    print(4)
