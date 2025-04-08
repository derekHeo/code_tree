m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.

Dow = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']

month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

A = sum(month[:m1]) + d1
B = sum(month[:m2]) + d2

if A > B:
    days = A-B
    dw = days % 7
    if dw == 0:
        print(Dow[1])
    elif dw == 1:
        print(Dow[0])
    elif dw >= 2:
        print(Dow[6+2-dw])

elif B > A:
    days = B-A
    dw = days % 7
    if dw == 0:
        print(Dow[1])
    elif dw == 6:
        print(Dow[0])
    elif dw >= 1:
        print(Dow[dw+1])

else:
    print('Mon')

