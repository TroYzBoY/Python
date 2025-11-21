# def palindrom():
#     word = input("ug : ")
#     if word == word[::-1]:
#         print("true")
#     else:
#         print("false")


# palindrom()


# def is_palindrom():
#     return s == s[::-1]


# s = input("string oruul :")
# print(is_palindrom())

# -------------------------------------------


# def unique_word_counter(sentence):
#     sentence = sentence.lower()
#     for i in [".", "!", "?", ","]:
#         sentence = sentence.replace(i, "")
#     words = sentence.split()
#     return len(set(words))


# a = input("oguulber e orul :")


# print(unique_word_counter(a))

# -------------------------------------------


# def matrix_sum():

#     matrix = [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ]
#     A = 0
#     for i in matrix:
#         for j in i:
#             A += j
#     return (A)


# print(matrix_sum())

# -------------------------------------------


# def tegsh():
#     num = int(input("too :"))
#     if num % 2 == 0:
#         print("tegsh")
#     else:
#         print("sondgoi")


# tegsh()

# -------------------------------------------


# def sondgoi():
#     num = int(input("too :"))
#     if num % 2 != 0:
#         print("sondgoi")
#     else:
#         print("tegsh")


# sondgoi()

# -------------------------------------------


# def neg_ees_n_hurtleh_niilber():
#     A = 0
#     for i in range(6):
#         A += i
#     print(A)


# neg_ees_n_hurtleh_niilber()

# -------------------------------------------


# def len():
#     A = 0
#     a = input("string oruul :")
#     for _ in a:
#         A += 1
#     print(A)


# len()


# -------------------------------------------


# def ih_too():
#     a = [1, 2, 3, 4, 5, 31, 2, 3, 5]
#     b = a[0]
#     for i in a:
#         if i > b:
#             b = i
#     print(b)


# ih_too()

# -------------------------------------------


# def baga_too():
#     a = [1, 2, 3, 4, 5, 31, 2, 3, 5]
#     b = a[0]
#     for i in a:
#         if i < b:
#             b = i
#     print(b)


# baga_too()

# -------------------------------------------


# def anhnii_too():
#     a = int(input("too :"))
#     if a % 2 and 3 and 5 and 7 != 0:
#         print("true")
#     else:
#         print("false")


# anhnii_too()

# -------------------------------------------


# def dundaj():
#     a = [2, 4, 6, 8]
#     b = sum(a) / len(a)
#     print(b)


# dundaj()

# -------------------------------------------


# def dawhtssan_too(a):

#     b = []
#     for i in range(len(a)):
#         count = 0
#         for j in range(len(a)):
#             if a[i] == a[j]:
#                 count += 1
#             if count > 1 and a[i] not in b:
#                 b.append(a[i])
#     return b


# number = [1, 2, 3, 2, 4, 1, 1]

# print(dawhtssan_too(number))

# -------------------------------------------


# def reverse():
#     word = str(input("string oruul :"))
#     print(str(word))


# reverse()

# --------------------------------------------


# def neg_ees_n_hurtleh_urjwer():
#     A = 1
#     n = int(input("too : "))
#     for i in range(1, n+1):
#         A *= i
#     print(A)


# neg_ees_n_hurtleh_urjwer()

# --------------------------------------------


# def str_dotorh_dawtagdsan_useg():
#     a = str(input("string oruul :"))
#     b = []
#     for i in range(len(a)):
#         count = 0
#         for j in range(len(a)):
#             if a[i] == a[j]:
#                 count += 1
#             if count > 1 and a[i] not in b:
#                 b.append(a[i])
#     return (b)


# print(str_dotorh_dawtagdsan_useg())

# --------------------------------------------


# def armstrong():
#     num = int(input(" too oruul :"))
#     numstr = str(num)
#     length = len(numstr)
#     total = 0
#     for i in numstr:
#         total += int(i) ** length
#     if total == num:
#         print("True")
#     else:
#         print("False")


# armstrong()

# --------------------------------------------


# def list_dotorh_sondgoi_toonii_niilber():
#     a = list(map(int, input("zaigaar tusgaarlan too oruul :").split(" ")))
#     A = 0
#     for i in a:
#         if i % 2 != 0:
#             A += i
#     print(A)


# list_dotorh_sondgoi_toonii_niilber()

# --------------------------------------------


# def array_ermble():
#     a = [4, 2, 7, 1]
#     b = sorted(a)
#     print(b)


# array_ermble()

# --------------------------------------------


# def palindrom():
#     word = input("ug : ")
#     if word == word[::-1]:
#         print("true")
#     else:
#         print("false")


# palindrom()

# --------------------------------------------


# def fibonacci(x):
#     if x == 0:
#         return 0
#     elif x == 1:
#         return 1
#     else:
#         return fibonacci(x-1) + fibonacci(x-2)


# n = int(input("too : "))
# for i in range(n):
#     print(fibonacci(i), end=", ")

# --------------------------------------------


# def a(x):
#     k = {}
#     for i in x:
#         if i in k:
#             k[i] += 1
#         else:
#             k[i] = 1
#     for i, j in k.items():
#         print(f"{i}={j}", end=", ")


# a("banana")

# --------------------------------------------


# def second_max(a):

#     first = second = float()
#     for i in a:
#         if i > first:
#             second = first
#             first = i
#         elif i > second and i != first:
#             i = second
#     return second


# numbers = [10, 4, 18, 20, 15]
# print(second_max(numbers))


# --------------------------------------------


# def even_odd():
#     lst = [1, 2, 3, 4, 5, 6]
#     even = []
#     odd = []
#     for i in lst:
#         if i % 2 == 0:
#             even.append(i)
#         else:
#             odd.append(i)
#     print(f"Even : {even}\nOdd  : {odd}")


# even_odd()

# -----------------------------------------------1 DUND TUWSHIN


# def is_prime(num):                       # Анхны тоо эсэхийг шалгах функц
#     if num < 2:                          # 2-оос бага бол анхны тоо биш
#         return False
#     for i in range(2, int(num**0.5) + 1):  # 2-с sqrt(num) хүртэл шалгана
#         if num % i == 0:                 # Хэрэв хуваагдвал анхны биш
#             return False
#     return True                          # Хуваагдахгүй бол анхны тоо


# def sum_of_primes(n):
#     total = 0
#     for i in range(2, n + 1):            # 2-с n хүртэл тоог шалгах
#         if is_prime(i):                  # Хэрэв анхны бол
#             total += i                   # нийлбэрт нэмэх
#     return total


# print(sum_of_primes(10))  # 👉 2+3+5+7 = 17

# -----------------------------------------------2


# def list_dotorh_hoyor_toonii_niilber():
#     lst = list(map(int, input("zaigaar tusgaarlan list oruul : ").split(" ")))
#     target = 5
#     for i in range(len(lst)):
#         for j in range(len(lst)):
#             if lst[i] + lst[j] == target:
#                 print(f"{lst[i]} + {lst[j]} = {target}")


# list_dotorh_hoyor_toonii_niilber()

# ------------------------------------------------3


# def str_dotorh_dawtagdsan_useg_has():
#     a = str(input("string oruul :"))
#     b = ""
#     for i in a:
#         if i not in b:
#             b += i
#     return (b)


# print(str_dotorh_dawtagdsan_useg_has())

# --------------------------------------------------4


# def list_dotorh_toonii_yalgawar():
#     lst = list(map(int, input("zaigaar tusgaarlan list oruul : ").split(" ")))
#     mini = lst[0]
#     maxi = lst[0]
#     for i in lst:
#         if i > maxi:
#             maxi = i
#         if i < mini:
#             mini = i
#     total = maxi - mini
#     print(total)


# list_dotorh_toonii_yalgawar()

# --------------------------------------------------5


# def massive_iig_eremble():
#     lst = list(map(int, input("zaigaar tusgaarlan list oruul : ").split(" ")))
#     if lst == sorted(lst) or sorted(lst[::-1]):
#         print("true")
#     else:
#         print("false")


# massive_iig_eremble()

# --------------------------------------------------6


# def palindrome():
#     word = str(input("ug oruul : "))
#     if word == word[::-1]:
#         print("true")
#     else:
#         print("False")


# palindrome()

# --------------------------------------------------7


# def second_max(a):

#     first = second = float()
#     for i in a:
#         if i > first:
#             second = first
#             first = i
#         elif i > second and i != first:
#             i = second
#     return second


# numbers = [10, 4, 18, 20, 15]
# print(second_max(numbers))

# --------------------------------------------------8


# def str_dotorh_dawtagdsan_useg():
#     a = list(map(int, input("zaigaar tusgaarlan list oruul : ").split(" ")))
#     b = []
#     for i in range(len(a)):
#         count = 0
#         for j in range(len(a)):
#             if a[i] == a[j]:
#                 count += 1
#             if count > 0 and a[i] not in b:
#                 b.append(a[i])
#     return (b)


# print(str_dotorh_dawtagdsan_useg())

# --------------------------------------------------9
