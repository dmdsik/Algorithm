'''
Greedy algorithm (탐욕 알고리즘)
"매 선택에서 지금 이 순간 당장 최적인 답을 선택하여 결과 도출"
즉, 매 선택이 그 순간에서는 최적이지만 전체로 봤을땐최적화가 잘 되지 않았을 수도
있다는 말이다.

'''
N = int(input())

arr = list(map(int, input().split()))

if N == 1:
    print(arr[0])
else:
    arr.sort() #sort()를 쓰면 오름차순으로 정렬

    i_sum = 0 
    min_sum = 0

    for i in range(N):
        min_sum += (i_sum + arr[i])
        i_sum += arr[i]

    print(min_sum) 