known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]

    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res





# class Student:
#     def __init__(self, name, iq, salary, height):
#         self.name = name
#         self.iq = iq
#         self.salary = salary
#         self.height = height

# class StudentBody:
#     def __init__(self):
#         self.students = []
#     def addStudent(self, student):
#         self.students.append(student)
#     # def nameOfSmartest(self):
#         # code will go here
#     # def funOfBest(self, fun, feature):
#         # code will go here

# jody = Student("Jody", 100, 100000, 80)
# chris = Student("Chris", 150, 40000, 62)
# dana = Student("Dana", 120, 2000, 70)
# aardvarkU = StudentBody()
# aardvarkU.addStudent(jody)
# aardvarkU.addStudent(chris)
# aardvarkU.addStudent(dana)

# def getBestAndTaller():
#     bestAndTaller = dict()
#     i = 0
#     while i < len(aardvarkU.students):
#         bestAndTaller[aardvarkU.students[i].name] = aardvarkU.students[i].iq + aardvarkU.students[i].height
#         i+=1
#     result = max(bestAndTaller, key=bestAndTaller.get)
#     return result