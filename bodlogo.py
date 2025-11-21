# a = float(input("too oruulna uu : "))
# if a>=0 :
#     print("eyreg")
# else :
#     print("sorog")

# -----------------------------------------------------

# sar = int(input("sar aa oruulna uu : "))
# if sar in (12, 1, 2) :
#     print("uwul")
# elif sar in (3, 4, 5) :
#     print("hawar")
# elif sar in (6, 7, 8) :
#     print("zun")
# elif sar <=0 :
#     print("sar bish")
# elif sar >=13 :
#     print("sar bish")
# else :
#     print("namar")

# ------------------------------------------------------

# a = int(input("number :D 1 : "))
# b = int(input("number 2 :D :"))
# print("ih too")
# if (a>b) :
#     print(a)
# else : print(b)
# print("baga too")
# if (a<b) :
#     print(a)
# else : print(b)

# -------------------------------------------------------

# a = int(input("number :D 1 : "))
# b = int(input("number 2 :D :"))
# c = int(input("number 3 :D :"))
# print("ih too")
# if (a>b>c) :
#     print(a)
# elif (a>c>b) :
#     print(a)
# elif (b>c>a) :
#     print(b)
# elif (b>a>c) :
#     print(b)
# elif (c>a>b) :
#     print(c)
# else :
#     print(c)

# -------------------------------------------------------

# a, b, c, d = map(int, input("zaigaar tusgaarlan 4 too oruul : ") .split(" "))
# p = min(a, b, c, d)
# print("baga too ni : ")
# print(p)

# ---------------------------------------------------------

# a, b, c, d = map(int, input("zaigaar tusgaarlan 4 too oruul : ") .split(" "))
# sum = (a + b + c + d)
# print("element : ")
# print(sum)

# ---------------------------------------------------------

# a = float(input("ehnii too 1 : "))
# b = float(input("ehnii too 2 : "))
# c = float(input("ehnii too 3 : "))
# d = float(input("ehnii too 4 : "))
# if (a<5, b<5, c<5, d<5) :
#     print(a * b * c * d)
# else :
#     print("none")

# ----------------------------------------------------

# 1 baiguulgiin 1m say aas 10% 1m->5m

# tsalin = int(input("tsalin : "))
# a = 1000001
# b = 5000001
# c = 10000001
# aa = 1000000
# bb = 5000000
# cc = 10000000
# A = 0
# if 0 < tsalin < a :              #1 say aas doosh A
#     A = (tsalin / 100) * 90
# if a < tsalin < b :           #1-5 say hurtleh A
#     A =(tsalin / 100) * 80
# if b < tsalin < c :           #5-10 say hurtleh A
#     A = (tsalin / 100) * 70
# if c < tsalin :               #10+ 4.3m
#     A = tsalin - ((aa / 100 * 10) + (bb / 100 * 20) + (cc / 100 * 30) + ((tsalin - cc) / 100 * 40))
# print(A)

# ----------------------------------------------------

# a,b,c = map(int, input("zaigaar tusgaarlan 3 too oruul : ") .split(" "))
# A = 0
# if a % 2 == 0 :
#     A += a
# elif b % 2 == 0 :
#     a += b
# elif c % 2 == 0 :
#     b += c
# print(A)

# -----------------------------------------------------

# fenrir = ("SyntaxError")
# print(fenrir)

# ------------------------------------------------------

# age = 18
# if age > 18 :
#     print ("vape tataj bolno")
# else :
#     print("vape tataj bolkushvv huurhnu <3")

# -----------------------------------------------------

# tsag = int(input("tsag a oruulna u : "))
# if tsag in (6, 7, 8, 9, 10, 11) :
#     print("ugluu")
# elif tsag in (12, 13, 14, 15, 16, 17) :
#     print("udur")
# elif tsag in (18, 19, 20, 21) :
#     print("oroi")
# elif tsag <=-1 :
#     print("yu ch bish")
# elif tsag >=25 :
#     print("yu ch bish")
# else :
#     print("shunu")

# ---------------------------------------------------------

# a = int(input("too oruulna uu : "))
# if a % 3 == 0:
#     print("true")
# else :
#     print("false")

# ---------------------------------------------------------

# a = int(input("too oruulna uu : "))
# if a % 5 == 0:
#     print("true")
# else :
#     print("false")

# ---------------------------------------------------------

# orolt =float(input("too oruulna u : "))
# a = orolt / 1000
# b = orolt / 100
# c = orolt / 10
# print(a, "KM", b, "DM", c, "CM")

# ----------------------------------------------------------

# orolt =float(input("too oruulna u : "))
# a = orolt / 1000
# b = orolt / 100
# c = orolt * 100
# if orolt >= 1000 :
#     print(orolt / 1000, "km")
# elif orolt >= 100 :
#     print(orolt/100, "dm")
# elif orolt >= 10 :
#     print(orolt/10, "cm")
# else :
#     print("(-)km dm cm gj baihgu buur bolomjgu")

# print(f"{a} KM {b} DM {c} CM")

# -----------------------------------------------------------

# for i in range (1, 6):
#     print(i)

# -----------------------------------------------------------

# a = map(int, input("zaigaar tusgaarlan 5 too oruul : ").split(" "))
# A = 0
# for i in a:
#     A += i
# print(A)

# -----------------------------------------------------------

# jims = ["banana", "apple", "orange", "kiwi", "pear"]
# print(jims)

# ----------------------------------------------------------

# jigsaalt = [1, -2, 3, 4, 31, 6, 7, 21, 9,10]
# a = jigsaalt[0]
# b = jigsaalt[0]
# for i in jigsaalt:
#     if i > a :
#         a = i
#     if i < b:
#         b = i

# print(a)
# print(b)

# ----------------------------------------------------------

# target 25

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# target = int(25)
# b = 0

# for i in a:
#     b += i
#     if b == target:
#         print(f"target : {b}")

# liist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# target = 25

# for i in range(len(liist)):
#     for i1 in range(len(liist)):
#         if liist[i] + liist[i1] == target:
#             print(f"{liist[i]} + {liist[i1]} = {target}")

# ----------------------------------------------------------

# matrix=[
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# for i in matrix :
#     for i1 in i:
#         print(i1, end=" ")
#     print()

# ----------------------------------------------------------

# def main_function(num):
#     def cube(x):
#         return x*x*x
#     def num_num(x):
#         return x*x
#     print("cube" , cube(num))
#     print("num" , num_num(num))
# main_function(2)

# ----------------------------------------------------------

# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird

# def sum_of_number(y) :
#     niilber = 0
#     for i in input("number : ") :
#         range(1, y+1)
#         niilber += i
#         return niilber
#     print(niilber)
# sum_of_number(1)

# ----------------------------------------------------------

# def digit_sum(n):
#     total = 0
#     for digit in str(n):
#         total += int(digit)
#     return total


# num = int(input("Тоог оруулна уу: "))
# print("Цифрийн нийлбэр =", digit_sum(num))

# ----------------------------------------------------------

# 2. N хүртэлх тооны факториал олох
# Өгүүлбэр: Хэрэглэгчээс нэг бүхэл тоо ав. Тэр тооны факториалыг олдог функц бич.


# def multiply_of_digit():
#     sum = int(input("тоо :"))
#     total = 1
#     for i in range(1, sum+1):
#         total *= i
#     print(total)


# multiply_of_digit()

# ----------------------------------------------------------

# 3. Тэгш ба сондгой тоо тоолох
# Өгүүлбэр: Хэрэглэгчээс N тоонууд ав. Жагсаалт дахь хэд нь тэгш, хэд нь сондгой тоо байгааг олдог функц бич.

# def even_odd():
#     a = list(map(int, input("Зайгаар тусгаарлан тоонууд оруул :").split(" ")))
#     even_total = 0
#     odd_total = 0
#     for i in a:
#         if i % 2 == 0:
#             even_total += 1
#         else:
#             odd_total += 1
#     print(f"Нийт тэгш тоо: {even_total} \nНийт сондгой тоо: {odd_total} ")


# even_odd()

# ------------------------------------------------------------------------

# 4. Палиндром үг шалгах
# Өгүүлбэр: Хэрэглэгчээс нэг үг ав. Өгөгдсөн үг палиндром
# (урд талаас уншихад ч, хойноос уншихад ч адил) эсэхийг шалгадаг функц бич.

# def palindrom():
#     word = str(input("үг оруул :"))
#     if word == word[::-1]:
#         print("palindrom")
#     else:
#         print("not palindrom")
#         return


# palindrom()

# ------------------------------------------------------------------------

# 5. Жагсаалтын хамгийн их ба бага утга олох
# Өгүүлбэр: Хэрэглэгчээс тоон жагсаалт ав. Жагсаалтын хамгийн их
# болон хамгийн бага тоог буцаадаг функц бич.

# 1.

# def triangle():
#     p1, p2, p3 = map(int, input("zaigaar tusgaarlan 3 too oruul :").split(" "))
#     return p1 + p2 + p3

# print(triangle())

# ------------------------------------------------------------------------

# 21

# def arr():
#     a = [1, 2, 3, 2, 4, 5, 1]
#     b = []
#     for i in range(len(a)):
#         count = 0
#         for j in range(len(a)):
#             if a[i] == a[j]:
#                 count += 1
#             if count > 1 and a[i] not in b:
#                 b.append(a[i])
#     print(b)


# arr()


# 22.

# def palindrome():
#     a = str(input("useg oruul"))
#     if a == a[::-1]:
#         print("Palindrome")
#     else :
#         print("Not palindrome")

# palindrome()

# 23.

# def max_subarray_sum(arr):
#     current_sum = arr[0]
#     max_sum = arr[0]

#     for i in range(1, len(arr)):
#         current_sum = max(arr[i], current_sum + arr[i])
#         max_sum = max(max_sum, current_sum)

#     return max_sum

# arr = [-2,1,-3,4,-1,2,1,-5,4]
# print(max_subarray_sum(arr))


# 24.

# def anagram():
#     a = str(input("string oruul : "))
#     b = str(input("string oruul : "))
#     if sorted(a) == sorted(b):
#         print("True")
#     else:
#         print("False")

# anagram()

# 25.

# def matrix():
#     a = []
#     i = [
#           [1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9]
#             ]
#     for i in range(len(i)):
#         for j in range(len(i[i])):
#             if i == j:
#                 a.append(i[i][j])
#     print(sum(a))


# matrix()

# 26.

# def anhnii_too():
#     a = int(input("too : "))
#     b = []
#     # эхний анхны тоонуудыг гараар нэмнэ
#     for x in [2, 3, 5, 7, 11]:
#         if x <= a:
#             b.append(x)
#     # 7-аас дээш тоонуудыг 2,3,5,7-д хуваагдахгүйг шалгана
#     for i in range(8, a + 1):
#         if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and i % 11 != 0:
#             b.append(i)
#     print(b)


# anhnii_too()


# a=15 % 5
# print(a)
# 27.

# def massive_min_max():
#     A = [5, 7, 2, 9, 4]
#     a = A[0]
#     b = A[0]
#     for i in A:
#         if i > a :
#           a = i
#         if i < b:
#             b = i
#     print(f"max -> {a}, min -> {b}")

# massive_min_max()

# 28.

# def arr():
#     x = str(input("str oruul : "))
#     k = {}
#     for i in x:
#         if i in k:
#             k[i] += 1
#         else:
#             k[i] = 1
#     for i, _ in k.items():
#         if k[i] < 2:
#             print(f"{i}", end=", ")

# arr()

# 29.

# def matrix():
#     mtx = [
#         [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9]
#     ]
#     max_sum = 0
#     max_row = []
#     for i in mtx:
#         row_sum = sum(i)
#         if row_sum > max_sum:
#             max_sum = row_sum
#             max_row = i
#     print(max_row)

# matrix()

# 30

# def decimal_to_binary():
#     n = int(input("decimal too oruul : "))
#     if n == 0:
#         return "0"
#     binary = ""
#     while n > 0:
#         binary = str(n % 2) + binary
#         n = n // 2
#         print(binary)


# decimal_to_binary()

# -----------------------------------------------
# MID LEVEL--------------------------------------

# 1.

# def fizzbuzz():
#     a = int(input("too oruul : "))
#     if a % 3 == 0 and a % 5 == 0:
#         print("FizzBuzz")
#     elif a % 3 == 0:
#         print("Fizz")
#     elif a % 5 == 0:
#         print("Buzz")
#     else:
#         print("False")

# fizzbuzz()

# 2.

# def word_max_len():
#     a = list(map(str, input("oguulber oruul : ").split()))
#     ug = max(a, key=len)
#     urt = len(ug)
#     print(f"ug    : {ug}")
#     print(f"urt ni: {urt}")

# word_max_len()


# 3.

# def anhnii_too():
#     a = int(input("too : "))
#     b = []
#     for x in [2, 3, 5, 7, 11]:
#         if x <= a:
#             b.append(x)
#     for i in range(11, a + 1):
#         if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and i % 11 != 0:
#             b.append(i)
#     print(b)


# anhnii_too()

# 4.

# def massive_dawhtaagu_tooni_niilber():
#     a = list(map(int, input("massive oruul: ").split()))
#     niilber = 0
#     for i in range(len(a)):
#         davtalt = 0
#         for j in range(len(a)):
#             if a[i] == a[j]:
#                 davtalt += 1
#         if davtalt == 1:
#                 niilber += a[i]
#     print(niilber)
# massive_dawhtaagu_tooni_niilber()

# 5.

# def sum_lambda():
#     students = [('Bat', 85), ('Bold', 92), ('Suren', 78)]
#     top_student = max(students, key=lambda x: x[1])
#     print("max sum student :", top_student[0], top_student[1])

# sum_lambda()


# 6.

# def a():
#     x = list(map(int, input("Massive oruul : ").split()))
#     y = list(map(int, input("Massive oruul : ").split()))
#     X = set(x)
#     Y = set(y)
#     print(Y & X)


# a()

# 7.

# def scores():
#     scores = {'Bat': 85, 'Bold': 92, 'Suren': 78, 'Naraa': 92}
#     max_score = max(scores.values())
#     top_students = [name for name, score in scores.items() if score == max_score]
#     for student in top_students:
#         print(f"Hamgiin undur onoo awsan suragch : {student}")

# scores()

# 8.

# def while_loop():
#     n = int(input("too : "))
#     total = 0
#     count = 0
#     while total <= n:
#         count += 1
#         total += count
#         print(f"too : {count}, niilber : {total}")

# while_loop()


# 9.

# def str_dict_counter():
#     x = str(input("string oruul : "))
#     k = {}
#     for i in x:
#         if i in k:
#             k[i] += 1
#         else:
#             k[i] = 1
#     for i, j in k.items():
#         print(f"{i}={j}", end=", ")


# str_dict_counter()

# 10.

# def create_phonebook():
#     phonebook = {}
#     n = int(input("hunii too : "))
#     for i in range(n):
#         name = input(f"{i+1}-r hunii ner : ")
#         number = input(f"{name} nii utasnii dugaar : ")
#         phonebook[name] = number

#     return phonebook


# def search_phonebook(phonebook):
#     while True:
#         search_name = input("haih hunii ner : ")
#         if search_name.lower() == "exit":
#             break
#         if search_name in phonebook:
#             print(f"{search_name}nii dugaar ni : {phonebook[search_name]}")
#         else:
#             print("tiim hun baihgueeee !!!")


# book = create_phonebook()
# search_phonebook(book)

# ------------------------------------------------------------------------------

# 1.

# def eyreg_surug():
#     n = int(input(" too : "))
#     if n == 0:
#         print("teg")
#     elif n > 0:
#         print("eyreg")
#     else:
#         print("surug")

# eyreg_surug()

# 2.

# def hoyor_tooni_ih():
#     n = map(int, input("zaigaar tusgaarglan 2 too oruu :").split())
#     print(max(n))
# hoyor_tooni_ih()

# 3.

# def uliral():
#     sar = int(input("sar aa oruulna uu : "))
#     if sar in (12, 1, 2) :
#         print("uwul")
#     elif sar in (3, 4, 5) :
#         print("hawar")
#     elif sar in (6, 7, 8) :
#         print("zun")
#     elif sar <=0 :
#         print("sar bish")
#     elif sar >=13 :
#         print("sar bish")
#     else :
#         print("namar")
#     return(sar)

# uliral()

# 4.

# def n_too_hurtleh_niilber():
#     n = int(input("too : "))
#     A = 0
#     for i in range(1, n+1):
#         A += i
#         print(A)

# n_too_hurtleh_niilber()

# 5.

# def n_hurtleh_toonii_niilber_duruwt_huwaagddag():
#     n = int(input("too : "))
#     A = 0
#     for i in range(1, n+1):
#         if i % 4 == 0:
#             A += i
#     print(A)

# n_hurtleh_toonii_niilber_duruwt_huwaagddag()

# 6.

# choice = int(input("too : "))
# if choice == 1:
#     print("")
# elif choice == 2:
#     print("")
# elif choice == 3:
#     print("")
# else:
#     print("")


# ===================================================================================================

# 1.

# def upper_str():
#     a = list(map(str, input("oguulber oruul :").split()))
#     b = []
#     for i in a:
#         b.append(i[0].upper() + i[1:].lower())
#     print(" ".join(b))


# upper_str()

# 2.

# def massive_positive_numbers():
#     a = [3, -1, 4, -2, 7]
#     b = []
#     for i in a:
#         if i > 0:
#             b.append(i)
#     print(b)

# massive_positive_numbers()

# 3.

# def faktorial(n):
#     count = 0
#     i = 5
#     while n // i > 0:
#         count += n // i
#         i *= 5
#     return count


# print(faktorial(10))

# 4.

# def arr_reverse():
#     a = [1, 2, 4, 3]
#     print(a.reverse())


# arr_reverse()

# 5.

# def arr_palindrome():
#     a = input("oguulber ee oruul : ").split()
#     s = "".join(a).lower()

#     if s == s[::-1]:
#         print("Palindrome")
#     else:
#         print("Not palindrome")

# arr_palindrome()

# 6.

# def massive_yalgaa():
#     lst = list(map(int, input("zaigaar tusgaarlan massive oruul :").split(" ")))
#     A = lst[0]
#     B = lst[0]
#     for i in lst:
#         if i > A:
#             A = i
#         if i < B:
#             B = i
#         print(A, B)


# massive_yalgaa()

# 7.

# def character_sum():
#     a = input("too : ")
#     total = 0
#     for i in a:
#         total += int(i)
#     print(total)


# character_sum()

# 8.


# 9.

# def student_dict_counter():
#     x = list(map(str, input("oguulber oruul : ").split()))
#     k = {}
#     for i in x:
#         if i in k:
#             k[i] += 1
#         else:
#             k[i] = 1
#     for i, j in k.items():
#         print(f"{i}={j}", end=", ")


# student_dict_counter()

# def sondgoi():
#     a = list(map(int, input("list oruul :").split()))
#     A = []
#     for i in a:
#         if i % 2 != 0:
#             A.append(i)
#     print(A)

# sondgoi()


# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return "хайсан тоо байхгүй байна!"
# nums = [1, 3, 5, 7, 9, 11, 13]
# print(binary_search(nums, 9))
# print(binary_search(nums, 11))
# print(binary_search(nums, 2))

# def n_hurtleh_too(n):
#     if n == 0:
#         return
#     n_hurtleh_too(n-1)
#     print(n)

# n_hurtleh_too(5)

###

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n-1)


# print(factorial(4))

###

# def n_hurtleh_niilber(n):
#     if n == 0 or n == 1:
#         return 1
#     return n + n_hurtleh_niilber(n-1)


# print(n_hurtleh_niilber(5))

###

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# for i in range(6):
#     print(fibonacci(i), end=", ")

###

# def reverse_string(s: str) -> str:
#     if len(s) <= 1:
#         return s
#     return reverse_string(s[1:]) + s[0]


# print(reverse_string("hello"))


###


# def find():
#     lst = []
#     for i in range(1, 11):
#         lst.append(i)
#         reverse_lst = lst[::-1]
#         print(reverse_lst)


# find()

# def find():
#     n = int(input())
#     total = 0
#     for i in range(1,11):
#         total += n
#         print(f"{n} * {i} = {total}")

# find()

