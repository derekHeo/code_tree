n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

result = [0]*200

for i in range(n):
    for j in range(segments[i][0]+100,segments[i][1]+100):
        result[j] += 1
    
print(max(result))