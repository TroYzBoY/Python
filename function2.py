x=int(input("x-ийн утга : "))
y=(4*x**2-3*x+5)

print(y)

N = int(input())

A = [0] * N
B = [0] * N
C = [0] * N

B[0] = A[0] + 1
C[0] = A[0] + B[0]

for i in range(1, N):
    A[i] = B[i - 1] * 2 + 1
    B[i] = A[i] + 1
    C[i] = A[i] + B[i]

for i in range(N):
    print(A[i], B[i], C[i])