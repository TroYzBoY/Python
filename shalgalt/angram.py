N,M,X,Y = map(int,input().split( ))

moves = [
    (1, 2), (1, -2), (-1, 2), (-1, -2),  # Moves with |dx|=1, |dy|=2
    (2, 1), (2, -1), (-2, 1), (-2, -1)   # Moves with |dx|=2, |dy|=1
]
count = 0

for ax, ay in moves:
    new_x = X + ax
    new_y = Y + ay
    if 1 <= new_x <= N and 1 <= new_y <= M:
        count += 1

print(count)

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

if n < 2:
    print("0")
elif len(a) < 2:
    print("0")
else:
    print(len(a)-1)
    if n < 2:
        print("0")
    elif len(b) < 2:
        print("0")
    else:
        print(len(b)-1)

a = map(int,input().split())

print(len(a))