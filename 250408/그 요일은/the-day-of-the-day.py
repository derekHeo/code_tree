m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.

Dow = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']

month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

x = sum(month[:m1]) + d1
y = sum(month[:m2]) + d2

idx = Dow.index(A)

if idx == 1:
    print(((y - x) // 7))
elif idx == 0:
    print(((y - x) // 7))
elif idx > ((y-x)%7)+1:
    print(((y-x) // 7))
elif idx <= ((y-x)%7)+1:
    print(((y-x) // 7) + 1)