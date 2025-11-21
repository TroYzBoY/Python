# 1.

# def triangle():
#     a, b, c = map(int, input("too :").split(" "))
#     sum = a+b+c
#     return sum


# print(triangle())

# 2.


# def sum_of_two():
#     a, b, = map(int, input("too :").split(" "))
#     sum = a+b
#     return sum


# print(sum_of_two())

# 3.

# def cube():
#     a = int(input("too :"))
#     result = a**3
#     return result

# print(cube())

# 4.

# def tegsh_untsugt():
#     a, b = map(int, input("too :").split(" "))
#     multiply = a * b
#     x = (a+b)*2
#     return(f"{multiply} talbai {x} premeeter")


# print(tegsh_untsugt())

# 5.


# def tegshitgel():
#     x = int(input("too : "))
#     y = 3 * x - 5
#     return y


# print(tegshitgel())


# 6.

# 4*x**2-3*x+5

# def tegshitgel_two():
#     x = int(input("too : "))
#     y = 4*x**2-3*x+5
#     return y


# print(tegshitgel_two())

# 7.

# def suuliin_tsifr():
#     x=int(input("тоо : "))
#     c=(x % 10)
#     return c


# print(suuliin_tsifr())

# 8.

# def aravtiin_oron():
# x=int(input("тоо : "))
# a=(x // 10)
# c=(a % 10)
# return c


# print(aravtiin_oron())

# 9.

# def multiply_of_two_digits():
#     a=int(input("2 оронтой тоо : "))
#     b=(a//10)
#     c=(a%10)
#     d=c*b
#     return d


# print(multiply_of_two_digits())

# 10.

# def sum_of_three_ditigs():
#     a = int(input("3 оронтой тоо: "))
#     b = ((a // 10) // 10)
#     c = ((a // 10) % 10)
#     d = a % 10
#     sum = b + c + d
#     return(sum)


# print(sum_of_three_ditigs())

# 11.

# def second_to_minute_n_second():
#     x = int(input("секунд оруул: "))
#     b = (x // 60)
#     c = (b * 60)
#     d = (x - c)
#     return (f"{b} minute, {d} second")


# print(second_to_minute_n_second())

# 12.

# def tsag_minute_second():
#     a = int(input("секунд оруул: "))
#     b = (a // 3600)
#     c = (b * 3600)
#     d = (a - c)
#     e = (d // 60)
#     f = (d - (e * 60))
#     return(f"{b} tsag {e} minute {f} second")


# print(tsag_minute_second())


# 13.

# def minute_second_to_second():
#     a, b = map(int, input("minute, second оруулна уу!:").split(" "))
#     c = (a * 60) + b
#     return(f"{c} second")

# print(minute_second_to_second())

# 14.

# def tsag_minute_second_to_second():
#     a, b, c = map(int, input("tsag oruulna uu :) :").split(" "))

#     d = (a * 3600) + (b * 60) + c
#     return(f"{d} second")

# print(tsag_minute_second_to_second())

# 15.

# def honog_tsag():
#     x = int(input("tsag oruulna uu :"))
#     honog = x // 24
#     a = honog * 24
#     tsag = x - a
#     return (f"{honog} honog {tsag} tsag")


# print(honog_tsag())

# 16.

# def honog_tsag_to_tag():
#     a, b = map(int, input("zaigaar tusgaarlan honog, tsag oruulna uu :").split(" "))
#     c = a * 24
#     sum = c + b
#     return(f"{sum} tsag")

# print(honog_tsag_to_tag())

# 17.

# def jil_sar():
#     sar = int(input("sar aa oruulna uu :"))
#     a = sar // 12
#     b = a * 12
#     c = sar - b
#     return(f"{a} jil {c} sar")

# print(jil_sar())

# 18.

# def jil_sar_to_sar():
#     jil, sar = map(int, input("zaigaar tusgaarlan jil sar oruulna uu :").split(" "))
#     a = jil * 12
#     sum = a + sar
#     return(f"{sum} sar")

# print(jil_sar_to_sar())

# 19.

# def ih_baga():
#     a, b = map(int, input("zaigaar tusgaarlan 2 too oruul :").split(" "))
#     if a < b:
#         print(b)
#     else:
#         print(a)


# print(ih_baga())


# 20.

# def ih_baga_baga():
#     a, b = map(int, input("zaigaar tusgaarlan 2 too oruul :").split(" "))
#     if a > b:
#         print(b)
#     else:
#         print(a)


# print(ih_baga_baga())

# 21.

# def gurvan_toonii_ih():
#     a, b ,c = map(int,input("zaigaar tusgaarlan 3 too oruul : ").split(" "))
#     if b<a>c :
#         return a
#     elif a<b>c :
#         return b
#     elif b<c>a :
#         return c

# print(gurvan_toonii_ih())


# OR

#     d = max(a, b, c)
#     return(f"{d} ih too")

# print(gurvan_toonii_ih())

# 22.

# def durwun_tooni_baga():
#     a, b, c, d = map(int, input("zaigaar tusgaarlan 4 too oruul : ") .split(" "))
#     p = min(a, b, c, d)
#     return(f"{p} baga too")


# print(durwun_tooni_baga())

# 23.

# def nayaas_ih_toonuudiin_niilber():
#     a, b, c, d = map(int, input("zaigaar tusgaarlan 4 too oruul : ") .split(" "))
#     A = 0
#     for i in [a, b, c, d]:
#         if i > 80:
#             A += i
#     return(f"niilber : {A}")


# print(nayaas_ih_toonuudiin_niilber())

# 24.

# def tawaas_baga_tooni_urjwer():
#     a, b, c, d = map(int, input("zaigaar tusgaarlan 4 too oruul : ") .split(" "))
#     A = 1
#     if a<5:
#         A *= a
#     if b<5:
#         A *= b
#     if c<5:
#         A *= c
#     if d<5:
#         A *= d
#     return(f"niilber : {A}")

# print(tawaas_baga_tooni_urjwer())

# 25.

# def tegsh_toonii_niilber():
#     a, b, c = map(int, input("zaigaar tusgaarlan 3 too oruul :").split(" "))
#     A = 0
#     if a % 2 == 0:
#         A += a
#     if b % 2 == 0:
#         A += b
#     if c % 2 == 0:
#         A += c
#     return(f"tesgh toonii niilber : {A}")


# print(tegsh_toonii_niilber())

# 26.

# def sondgoi_toonii_urjwer():
#     a, b, c = map(int, input("zaigaar tusgaarlan 3 too oruul :").split(" "))
#     A = 1
#     if a % 2 != 0:
#         A *= a
#     if b % 2 != 0:
#         A *= b
#     if c % 2 != 0:
#         A *= c
#     return(f"sondgoi toonii urjwer : {A}")

# print(sondgoi_toonii_urjwer())

# 27.

# def tavtai_tentsuu_too():
#     a, b, c = map(int, input("zaigaar tusgaarlan 3 too oruul :").split(" "))
#     A = 0
#     if a == 5:
#         A += 1
#     if b == 5:
#         A += 1
#     if c == 5:
#         A += 1
#     return(f"tavtai tentsuu too : {A}")

# print(tavtai_tentsuu_too())

# 28.

# def gurawd_huwaggdag_toonuud():
#     a, b, c, d = map(int, input("zaigaar tusgaarlan 3 too oruul :").split(" "))
#     A = 0
#     if a % 3 == 0:
#         A += 1
#     if b % 3 == 0:
#         A += 1
#     if c % 3 == 0:
#         A += 1
#     if d % 3 == 0:
#         A += 1
#     return(f"3d huwaagddag too : {A}")

# print(gurawd_huwaggdag_toonuud())

# 29.

# def arwannegd_huwagddagu_tooni_niilber():
#         a, b, c, d = map(int, input("zaigaar tusgaarlan 3 too oruul :").split(" "))
#         A = 0
#         if a % 11 != 0:
#            A += a
#         if b % 11 != 0:
#             A += b
#         if c % 11 != 0:
#             A += c
#         if d % 11 != 0:
#             A += d
#         return(f"11 d huwaagddagu toonii niilber : {A}")


# print(arwannegd_huwagddagu_tooni_niilber())

# 30.

# def arawaas_ih_bol_yes():
#     num = int(input("too :"))
#     if num > 10:
#         print("YES")
#     else :
#         print("NO")


# print(arawaas_ih_bol_yes())

# 31.

# def tavaas_baga_bol_yes():
#     num = int(input("too :"))
#     if num < 5:
#         print("YES")
#     else :
#         print("NO")


# print(tavaas_baga_bol_yes())

# 32.

# def tegsh_bol_yes():
#     a, b, c = map(int, input("zaigaar tusgaarlan 3 too oruul :").split(" "))
#     if a % 2 == 0:
#         print(a, "YES")
#     else :
#         print(a, "NO")
#     if b % 2 == 0:
#         print(b, "YES")
#     else :
#         print(b, "NO")
#     if c % 2 == 0:
#         print(c, "YES")
#     else :
#         print(c, "NO")

# print(tegsh_bol_yes())

# 33.

# def lol():
#     print("I0I")

# print(lol())

# 34.

# def lol_for_guraw():
#     a = "I0I"
#     for _ in range(3):
#         print(a)

# lol_for_guraw()

# 35.

# def lol_for_guraw():
#     a = "I0I"
#     b = int(input("too : "))
#     for _ in range(b):
#         print(a)

# lol_for_guraw()


# 36.

# def n_toonii_niilber():
#     n = int(input("too oruul : "))
#     A = 0
#     for i in range(n+1):
#         A += i
#     return(A)

# print(n_toonii_niilber())

# 37.

# def n_toonii_urjwer():
#     n = int(input("too oruul : "))
#     A = 1
#     for i in range(n):
#         A *= i+1
#     return (A)


# print(n_toonii_urjwer())

# 38.

# def zuu_g_n_udaa_nem():
#     n = int(input("too :"))
#     a = 0
#     for _ in range(n):
#         a += 100
#     return(a)


# print(zuu_g_n_udaa_nem())


# 39.

# def a_toog_n_udaa_nem():
#     a, n = map(int, input("zaigaar tusgaarlan 2 too oruul : ").split(" "))
#     A = 0
#     for _ in range(n):
#         A += a
#     return(A)

# print(a_toog_n_udaa_nem())


# 40.

# def toonii_zereg():
#     n = int(input("too :"))
#     eq = 2**n
#     return(eq)

# print(toonii_zereg())

# 41.

# def a_tooni_n_zereg():
#     a, n = map(int, input("zaigaar tusgaarlan 2 too oruul :").split(" "))
#     A = 1
#     for _ in range(n):
#         A *= a
#     return(A)

# print(a_tooni_n_zereg())

# 42.

# def tentssen():
#     orolt = int(input(" too:"))
#     if 3 <= orolt < 6 :
#         print("tentssen")
#     elif 3 > orolt > 1:
#         print("unasan")
#     else :
#         print("2-5 hurtel too oruulna uu!!")
#     return(orolt)

# tentssen()

# 43.

# def onts_sain_muu():
#     orolt = int(input(" too:"))
#     if orolt == 2:
#         print("muu")
#     elif orolt == 3:
#         print("dund")
#     elif orolt == 4:
#         print("sain")
#     elif orolt == 5:
#         print("onts")
#     else :
#         print("2-5 hurtel too oruulna uu!!")


# onts_sain_muu()

# 44.

# def score():
#     score =float(input("score: "))

#     if score >= 90:
#         print("(A) aimar shvv kkk")
#     elif score >= 80:
#         print ("B")
#     elif score >=70 :
#         print ("C")
#     else :
#         print("(F) (GG arai2)")
#     return(score)

# score()

# 45.

# def day():
#     orolt = int(input("udur oruulna uu :"))
#     if orolt == 1:
#         print("Monday")
#     elif orolt == 2:
#         print("Tuesday")
#     elif orolt == 3:
#         print("Wednesday")
#     elif orolt == 4:
#         print("Thursday")
#     elif orolt == 5:
#         print("Friday")
#     elif orolt == 6:
#         print("saturday")
#     elif orolt == 7:
#         print("Sunday")
#     else :
#         print("1-7 hurtel udur oruulna uu!!")
#     return(orolt)

# day()

# 46.

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

# 47.

# def gurwaljinn():
#     a, b, c = map(int, input(" zaigaar tusgaarlan 3 too oruul :").split(" "))
#     if a + b > c and a + c > b and b + c > a:
#         print("YES")
#     else:
#         print("NO")


# gurwaljinn()

# 48.

# def hvrd():
#     n = int(input("too :"))
#     for i in range(1, 11):
#         print(f"{n}*{i}={n*i}")

# hvrd()


# 49.

# def zereg():
#     n = int(input("too :"))
#     for i in range(1, 6):
#         print(f"{n}**{i}={n**i}")

# zereg()


# 50.

# def ilerhiilel(a, b, c):

#     A = a*b-c
#     return A


# print(ilerhiilel(1, 2, 3))


# 51. =====================================

# def haalga_toot():
#     a, b = map(int, input("zaigaar tusgaarlan 2 too :").split(" "))
#     c = int(input("toot :"))
#     aa = a * b
#     d = c // b
#     f = c-(d * b)
#     if aa >= c >= 1:
#         print(f"{d+1} dawhar {f} toot")
#     else:
#         print("t1 hun huurj bga yu chi !")


# haalga_toot()