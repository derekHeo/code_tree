m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.

m_list = [31,28,31,30,31,30,31,30,31,30,31,30]

print((sum(m_list[:m2-1]) + d2) - (sum(m_list[:m1-1])+ d1))