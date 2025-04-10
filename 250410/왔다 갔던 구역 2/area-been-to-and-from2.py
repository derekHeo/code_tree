n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.
right_max = 0
left_max = 0
for i in range(n):
    if dir[i] == 'R':
        right_max += x[i]
    else:
        left_max += x[i]

max_len = right_max + left_max
result = [0] * (max_len+100)

start = max_len - abs(right_max-left_max) -1
start_right = start + 1
start_left = start

for i in range(n):
    if dir[i] == 'R':
        for pos in range(x[i]):
            result[start_left] += 1
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