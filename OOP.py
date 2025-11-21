# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score

#     def get_grade(self):
#         if self.score >= 60:
#             return "Pass"
#         else:
#             return "Fail"

# student1 = Student("Temuulen", 100)
# student2 = Student("Boru", 29)

# print(f"{student1.name} : {student1.get_grade()} {student1.score}")
# print(f"{student2.name} : {student2.get_grade()} {student2.score}")


##########

# class person:
#     def __init__(self, teacher):
#         self.teacher = teacher


# class teacher(person):
#     def teach(self):
#         print(f"{teacher1.teacher} is teaching")
#         print(f"{teacher2.teacher} is teaching")


# teacher1 = teacher("Neo")
# teacher2 = teacher("ChiLLeViL")

# teacher1.teach()

############

# class shape:
#     def __init__(self):
#         raise NotImplementedError


# class circle(shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * (self.radius ** 2)


# class rectangle(shape):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def area(self):
#         return self.x * self.y


# circl = circle(5)
# qwe = rectangle(4, 6)
# print(circl.area())
# print(qwe.area())

# class Stack:
#     def __init__(self):
#         self._data = []

#     def push(self, x):
#         self._data.append(x)  # O(1)

#     def pop(self):
#         return self._data.pop()  # O(1), хоосон эсэхийг шалга

#     def peek(self):
#         return self._data[-1]

#     def is_empty(self):
#         return len(self._data) == 0


# s = Stack()
# s.push(10)
# s.push(20)
# print(s.pop())  # 20

