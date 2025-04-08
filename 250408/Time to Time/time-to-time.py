a, b, c, d = map(int, input().split())

# Please write your code here.

max_time = c * 60 + d
min_time = a * 60 + b

print(max_time - min_time)