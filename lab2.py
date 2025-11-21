# 2. Anagram Grouping (Dictionary ашиглах)
# Өгөгдсөн үгсийн жагсаалтыг авч, анаграм үгсийг нэг dict–д бүлэглэ.
# words = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Гаралт:
# {
# "aet": ["eat", "tea", "ate"],
# "ant": ["tan", "nat"],
# "abt": ["bat"]
# }

# def __dict__():
#     words = ["eat", "tea", "tan", "ate", "nat", "bat"]
#     for i in words:

# def unique_subarray_sum(nums):
#     sums = set()
#     n = len(nums)
#     for i in range(n):
#         total = 0
#         for j in range(i, n):
#             total += nums[j]
#             sums.add(total)
#     return len(sums)


# print(unique_subarray_sum([1, 2, 3, 4, 5]))


# def anagram(words):
#     groups={}
#     for word in words:
#         key = " ".join(sorted(word))
#         if key not in groups :
#             groups[key]= []
#         groups[key].append(word)
#     return groups
# words = ["eat", "tea", "tan", "ate", "nat", "bat"]


# print(anagram(words))


# def student_ranking(score):
#     return sum(score) / len(score)

# students = {
#     "tami": [85, 90, 78],
#     "ami": [92, 88, 95],
#     "dodo": [70, 75, 80]
# }
# a = []
# for name, scores in students.items():
#     b = student_ranking(scores)
#     a.append((name, b))
# a.sort(key=lambda x: x[1], reverse=True)
# top_student = a[0][0]
# for name, b in a:
#     if name == top_student:
#         print(f"Top student: {name} scolarship{b}")
#     sorted_scores = sorted(scores, reverse=True)
#     print(f"{name}: {', '.join(map(str, sorted_scores))}")

# def spiral_order(matrix):   # matrix гэдэг 2D жагсаалтыг спираль дарааллаар унших функц
#     res = []                # HOOSON MASSIV VVSGEJ HADGALNA IISHEE
#     left, right = 0, len(matrix[0]) - 1   # BAGANII EHLEL BA TOGOSGOL
#     top, bottom = 0, len(matrix) - 1      # MORIIN EHLEL BA TOGOSGOL

#     # HOYR HYZGAAR OGTLOLTSOHGVI BOL VRGELJILNE
#     while left <= right and top <= bottom:
#         # 1. TOP IIN ZVVNEES  BARUUN TIISHEE YWNAAAA
#         for c in range(left, right + 1):
#             res.append(matrix[top][c])
#         top += 1   # DEED MOR DUUSSAN BOL BOLHOOR DOOD TALIIHIIH RUU YWNAA

#         # 2. BARUUNAAS DOOSH DEEREES DOOSHOO YWNAA
#         for r in range(top, bottom + 1):
#             res.append(matrix[r][right])
#         right -= 1   # BARUUN BAGANIIG UNSHAAD DUUSTSAN BOLHOOR ZVVN TAL RUU NI ORNOO

#         # 3. DOOSHOO BARUUNAAS ZVVN TIISHEE YWNAA MOR VLDSEN BOL SHVVV
#         if top <= bottom:
#             for c in range(right, left - 1, -1):
#                 res.append(matrix[bottom][c])
#             bottom -= 1   # DOOD TALIIG NI UNSHSAN BOLHOOR DEESHEE TATNA

#         # 4. ZVVNEES DEESHEE DOOROOS_DEESH BAGANA VLDSEN BOL
#         if left <= right:
#             for r in range(bottom, top - 1, -1):
#                 res.append(matrix[r][left])
#             left += 1  # ZVVN BAGANIIG DUUSSAN BOL DOTOGSHOO YWNAA

#     return res

# # GGEZ


# matrix = [
#     [2, 1, 3],
#     [5, 6, 4],
#     [9, 7, 8]
# ]

# print(spiral_order(matrix))


# def dict_to_flat():
#     data = {
#      "user": {
#      "name": "Naraa",
#      "info": {
#      "age": 20,
#      "city": "UB"
#      }
#      }
#     }
