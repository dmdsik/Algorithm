'''
A,B,C는 21억 이하의 자연수
손익분기점이 존재하지 않으면 -1을 출력
A = 고정비용
B = 가변비용
C = 총 수입

손익 = A + Bn = Cn
C가 올라가면 언제는 A+Bn보다 Cn이 커지게 된다.

한 번 걸러줄 수 있는 조건
B>=C 이면 영원히 손익분기점이 발생하지 않겠죠(A라는 존재 때문에)
A는 양의 자연수
'''

A, B, C = map(int, input().split())

if B>=C:
    print(-1)
else:
    print(int(A/(C-B)+1))

