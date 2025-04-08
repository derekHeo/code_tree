m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dates = (sum(num_of_days[:m2]) + d2) - (sum(num_of_days[:m1]) + d1) + 1
print(dates)