m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.

m_list = [0,31,28,31,30,31,30,31,30,31,30,31]

print((sum(m_list[:m2]) + d2) - (sum(m_list[:m1]) + d1))