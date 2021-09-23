n = int(input())

chk = n
new = 0
temp = 0
count = 0
while True:
    temp = n//10 + n%10
    new = (n%10)*10 + temp%10
    count += 1
    n = new
    if new == chk:
        break
print(count)

