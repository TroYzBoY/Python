# def fib_dp(n):
#     # Суурь тохиолдлууд
#     if n <= 1:
#         return n

#     # Хүснэгт үүсгэх - dp[i] нь i-р Фибоначчийн тоог хадгална
#     dp = [0] * (n + 1)

#     # Суурь утгууд
#     dp[0] = 0  # F(0) = 0
#     dp[1] = 1  # F(1) = 1

#     # Доороос дээш тооцоолох - F(2), F(3), ..., F(n)
#     for i in range(2, n + 1):
#         dp[i] = dp[i-1] + dp[i-2]  # F(i) = F(i-1) + F(i-2)

#     return dp[n]

# # Туршилт
# print(fib_dp(5))  # Үр дүн: 5
# print(fib_dp(40)) # Шууд гарна! ⚡
# print(fib_dp(100)) # Энэ ч бас шууд гарна!

###############################

# def climb_ways(n):
#     if n <= 2:
#         return n
#     a, b = 1, 2
#     for _ in range(3, n + 1):
#         a, b = b, a + b
#     return b

# print(climb_ways(5))

###############################

# def min_cost():
#     cost = list(map(int, input("massive : ").split(" ")))
#     prev1, prev2 = cost[0], cost[1]
#     for i in range(2, len(cost)):
#         curr = cost[i] + min(prev1, prev2)
#         prev2, prev1 = prev1, curr
#     print( min(prev1, prev2))


# min_cost()

###############################

# def robber():
#     n = list(map(int,input("massive : ").split(" ")))
#     if not n:
#         return 0
#     if len(n) == 1:
#         return n[0]

#     prev2 = n[0]
#     prev1 = max(n[0], n[1])

#     for i in range(2, len(n)):
#         curr = max(prev1, prev2 + n[i])
#         prev2, prev1 = prev1, curr

#     return prev1


# robber()

###############################

