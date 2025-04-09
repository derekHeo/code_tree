N, B = map(int, input().split())

# Please write your code here.
result = []
while 1:
    if N < B:
        result.append(N)
        break

    result.append(N % B)
    N = N // B

for r in result[::-1]:
    print(r, end = '')