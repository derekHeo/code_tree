N = input()

# Please write your code here.

num = 0

for n in str(N):
    num = num * 2 + int(n)

new_num = num * 17
result = []

while 1:
    if new_num < 2:
        result.append(new_num)
        break
    result.append(new_num%2)
    new_num = new_num//2

for r in result[::-1]:
    print(r,end='')