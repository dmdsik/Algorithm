arr = []
for i in range(10):
    n = int(input()) #숫자 입력 받기
    arr.append(n%42) #append로 배열에 넣어주기
arr = set(arr) #set함수로 '집합'자료형 만들기(중복제거의 기능)
print(len(arr)) #함수의 길이(원소 갯수)

