# ###################### TASK 1

# data = [42, 3.14, "indra", [1,2,3], (1,2,3), {"a":1}, {1,2,3}]
# for x in data:
#     try:
#         print(f"{x} ✅ Hash value:", hash(x))
#     except:
#         print(f"{x} ❌ Unhashable object")

# ###################### TASK 2

# data = [
#     (1, 2, 3),
#     (1, [2, 3]),
#     ("indra", (5,6)),
#     ([1,2], "hi"),
#     ((1,2), (3,4))
# ]

# for x in data:
#     try:
#         print(f"{x} ✅ Hash:", hash(x))
#     except:
#         print(f"{x} ❌ Unhashable (contains mutable data)")

# ####################### TASK 3

# test_keys = [1, "key", (1,2), [3,4], {"x":5}]
# for k in test_keys:
#     try:
#         my_dict = {k: "value"}
#         print(f"{k} ✅ can be a key")
#     except:
#         print(f"{k} ❌ cannot be a key")
