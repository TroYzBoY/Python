# #################### TASK 1

# def bubble_sort(arr):
#     a = arr.copy()
#     n = len(a)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if a[j] > a[j + 1]:
#                 a[j], a[j + 1] = a[j + 1], a[j]
#     return a

# print(bubble_sort())



# ################### TASK 2


# def selection_sort_with_swaps(arr):
#     a = arr.copy()
#     n = len(a)
#     swaps = 0
    
#     for i in range(n):
#         min_index = i
#         for j in range(i + 1, n):
#             if a[j] < a[min_index]:
#                 min_index = j

#         if min_index != i:
#             a[i], a[min_index] = a[min_index], a[i]
#             swaps += 1

#     return a, swaps

# sorted_arr, swap_count = selection_sort_with_swaps()
# print("Эрэмбэлэгдсэн массив:", sorted_arr)
# print("Нийт солилт:", swap_count, "удаа")


# ################### TASK 3

# def bubble_with_stats(arr):
#     a = arr.copy()
#     swaps = 0
#     comparisons = 0
#     n = len(a)

#     for i in range(n):
#         for j in range(n - i - 1):
#             comparisons += 1
#             if a[j] > a[j + 1]:
#                 a[j], a[j + 1] = a[j + 1], a[j]
#                 swaps += 1

#     return a, swaps, comparisons

# ################### TASK 4

# nums = []
# for i in range(5):
#     n = int(input(f"{i+1}-р тоог оруул: "))
#     nums.append(n)

# print("Оруулсан тоонууд:", nums)

# bubble = bubble_sort(nums)
# print("Bubble Sort →", bubble)
# print("Python sorted() →", sorted(nums))

# ################### TASK 5

# def insertion_desc(arr):
#     a = arr.copy()
#     for i in range(1, len(a)):
#         key = a[i]
#         j = i - 1

#         # key-ээс бага бол баруун тийш шилжүүлнэ
#         while j >= 0 and a[j] < key:
#             a[j+1] = a[j]
#             j -= 1

#         a[j+1] = key

#     return a

# result = insertion_desc([5, 2, 9, 1, 5, 6])
# print("Эрэмбэлэгдсэн массив:", result)
