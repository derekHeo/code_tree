n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.

result = [0]*n

for i in range(k):
    for j in range(commands[i][0],commands[i][1]+1):
        result[j] += 1
print(max(result))