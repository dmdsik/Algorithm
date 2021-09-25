max_num = 0
num_index = 0

for i in range(9):
    a = int(input())

    if(a>max_num):
        max_num = a
        num_index = i + 1

print('%d\n%d'%(max_num, num_index))