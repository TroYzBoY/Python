# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1

# data = [12, 45, 23, 67, 89, 90]
# target = 67
# result = linear_search(data, target)

# if result != -1:
#     print(f"{target} тоо {result}-р индекс дээр байна.")
# else:
#     print("Олдсонгүй.")

# ############################

# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         print(f"Left={left}, Mid={mid}, Right={right}")

#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

#     return -1

# data = [1, 3, 5, 7, 9, 11, 13]
# print(binary_search(data, 9))

# ############################

# def binary_search_recursive(arr, target, left, right):
#     if left > right:
#         return -1

#     mid = (left + right) // 2

#     if arr[mid] == target:
#         return mid
#     elif arr[mid] < target:
#         return binary_search_recursive(arr, target, mid + 1, right)
#     else:
#         return binary_search_recursive(arr, target, left, mid - 1)
    