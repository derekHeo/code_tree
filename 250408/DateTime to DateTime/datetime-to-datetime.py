a, b, c = map(int, input().split())

# Please write your code here.

day_gap = a - 11

if day_gap == 0:
    gap = (b * 60 + c) - (11 * 60 + 11)
    if gap < 0:
        print(-1)
    else:
        print(gap)

else:
    print((b * 60 + c) - (11 * 60 + 11) + (60 * 24))