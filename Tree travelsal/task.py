# ####################### TASK 1

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


# ####################### TASK 2


# def inorder(node):
#     if node:
#         inorder(node.left)        # 1. Зүүн child
#         print(node.value, end=" ") # 2. Root хэвлэх
#         inorder(node.right)       # 3. Баруун child

# print("In-order Traversal:")
# inorder(root)


# ####################### TASK 3


# def preorder(node):
#     if node:
#         print(node.value, end=" ")  # Root
#         preorder(node.left)         # Left
#         preorder(node.right)        # Right

# print("\nPre-order Traversal:")
# preorder(root)


# ####################### TASK 4


# from collections import deque

# def level_order(node):
#     if not node:
#         return
    
#     queue = deque([node])
#     level = 1

#     while queue:
#         level_size = len(queue)
#         print(f"Level {level}:", end=" ")

#         for _ in range(level_size):
#             current = queue.popleft()
#             print(current.value, end=" ")

#             if current.left:
#                 queue.append(current.left)
#             if current.right:
#                 queue.append(current.right)

#         print()
#         level += 1

# print("\nLevel Order Traversal:")
# level_order(root)
