n = int(input())

# Please write your code here.
result = []
while 1:
    if n < 2:
        result.append(n)
        break
    result.append(n%2)
    n = n//2

for r in result[::-1]:
    print(r, end ='')