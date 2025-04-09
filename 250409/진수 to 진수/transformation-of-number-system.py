a, b = map(int, input().split())
n = input()

# Please write your code here.

num = 0
for s in str(n):
    num = num * 8 + int(s)

result = []
while 1:
    if num < b:
        result.append(num)
        break
    result.append(num%b)
    num = num // b

for r in result[::-1]:
    print(r,end='')