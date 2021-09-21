N, X = map(int, input().split())
A = list(map(int, input().split())) 
#You must memorize the grammer of the map()


for i in range(N):
    if A[i] < X:
        print(A[i], end = " ") #Python automatically newline, u don't need to newline then use <end = " ">
