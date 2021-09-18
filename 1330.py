a, b = input().split()

a = int(a)
b = int(b)

if a > b:
    print('>')
elif a < b:
    print('<')
else: #When you use "else" there rn't no condition
    print('==')