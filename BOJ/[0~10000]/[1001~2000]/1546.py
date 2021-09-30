n = int(input())
list_score = list(map(int, input().split()))
max_score = max(list_score)

modified_score = []
for score in list_score:
    modified_score.append(score/max_score*100)
average_score = sum(modified_score)/n
print(average_score)