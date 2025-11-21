# def linear_search():
#     arr = list(map(int, input().split()))
#     target = int(input())
#     index = 1
#     for i in range(len(arr)):

#         if arr[i] != target:
#             print(f"-1")
#         else:
#             print(f"olson2")
#             index += 1
#     print(f"haisan integer : {target}\nindex : {index}")


# linear_search()


################################################


# def binary_search():
#     arr = list(map(int, input().split()))
#     target = int(input())
#     lst = sorted(arr)
#     left, right = 0, len(lst) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if lst[mid] == target:
#             print(mid + 1)
#             return
#         elif lst[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     print("baihugui")


# binary_search()

################################################


# def character_count():
#     s = str(input("string oruul : "))
#     target = {}
#     char_dict = {}
#     for char in s:
#         if char in char_dict:
#             char_dict[char] += 1
#         else:
#             char_dict[char] = 1
#     for char, count in char_dict.items():
#         print(f"'{char}': {count}")


# character_count()

################################################

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# # Мод үүсгэх
# root = Node(8)
# root.left = Node(3)
# root.right = Node(10)
# root.left.left = Node(1)
# root.left.right = Node(6)
# root.left.right.left = Node(4)
# root.left.right.right = Node(7)
# root.right.right = Node(14)
# root.right.right.left = Node(13)

# # 🔹 In-order Traversal функц
# def inorder(node):
#     if node:
#         # 🔸 1. Зүүн child руу ор
#         inorder(node.left)
#         # 🔸 2. Root-ыг хэвлэ
#         print(node.value, end=" ")
#         # 🔸 3. Баруун child руу ор
#         inorder(node.right)

# print("In-order Traversal:")
# inorder(root)
# print()  # Шинэ мөр

# # 🎯 5 гэсэн node нэмэх (4 ба 6-ын хооронд байх ёстой)
# root.left.right.left.right = Node(5)

# print("\n\n5-г нэмсний дараах In-order Traversal:")
# inorder(root)
# print()

# def preorder(node):
#     if node:
#         # 🔸 1. Root-ыг эхлээд хэвлэ
#         print(node.value, end=" ")
#         # 🔸 2. Зүүн child руу ор
#         preorder(node.left)
#         # 🔸 3. Баруун child руу ор
#         preorder(node.right)

# print("\n\nPre-order Traversal:")
# preorder(root)

# # 🔹 Task 3 — Post-order Traversal (Left → Right → Root)
# def postorder(node):
#     if node:
#         # 🔸 1. Зүүн child руу ор
#         postorder(node.left)
#         # 🔸 2. Баруун child руу ор
#         postorder(node.right)
#         # 🔸 3. Root-ыг хамгийн сүүлд хэвлэ
#         print(node.value, end=" ")

# print("\n\nPost-order Traversal:")
# postorder(root)
# print()

################################################

