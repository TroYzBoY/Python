
# n = int(input())

# A = [0] * n
# B = [0] * n
# C = [0] * n
# B[0] = A[0] + 1
# C[0] = A[0] + B[0]

# for i in range(n):
#     if i == 0:
#         A[0] = 0
#         B[0] = A[0] + 1
#         C[0] = A[0] + B[0]
#     else:
#         A[i] = B[i - 1] * 2 + 1
#         B[i] = A[i] + 1
#         C[i] = A[i] + B[i]

#     print(A[i], B[i], C[i])

##############################################




a = int(input().split())
b = int(input().split())

A = sorted(a)
B = sorted(b)

