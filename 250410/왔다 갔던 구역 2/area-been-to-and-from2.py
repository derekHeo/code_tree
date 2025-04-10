n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

num = 0
num_list = []
# Please write your code here.
for i in range(n):
    if dir[i] == 'R':
        num += x[i]
        num_list.append(num)
    else:
        num -= x[i]
        num_list.append(num)

start = abs(min(num_list))
start_right = start + 1
start_left = start

result = [0]*(abs(min(num_list))+max(num_list)+100)
for i in range(n):
    if dir[i] == 'R':
        for pos in range(x[i]):
            result[start_right] += 1
            start_left += 1
            start_right += 1
    elif dir[i] == 'L':
        for pos in range(x[i]):
            result[start_left] += 1
            start_left -= 1
            start_right -= 1

count = 0
for t in result:
    if t >= 2:
        count += 1
print(count)