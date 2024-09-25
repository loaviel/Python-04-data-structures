print("Exercise 1")
#Create a Python list that stores the numbers 1-10 in indivdual elements.
#Then print out the contents of the list to check the values have been stored correctly.
#Extension: make use of an appropriate list method to reverse the order of this list.

numList = [1,2,3,4,5,6,7,8,9,10]
numList.reverse()
for i in numList:
    print(i)


print("\nExercise 2")
#Create a Python dictionary which stores the price for three items of food. 
#For example; milk is £1.30, pasta is £0.75, and strawberries are £1.50. 
#Output the dictionary to check the values are stored, 
#and then see if you can access the price for one of the items by using the item name as the 'key'.
#Extension: Now add a new key and value pair to previously defined dictionary.


dictionaryTest = {"milk" : "£1.30", "pasta" : "£0.75", "strawberries" : "£1.50"}
dictionaryTest["bananas"] = "£1.20"
print(dictionaryTest["bananas"])


print("\nExercise 3")
#Given two sets (prices and food names), can you create a dictionary that uses the foodnames as keys, and the prices as values?


foodnames = ["milk", "pasta", "strawberries"]
prices = [1.30, 0.75, 1.50]

foodInfo = {}


for i in range(len(foodnames)):
    foodInfo[foodnames[i]] = prices[i] 

print(foodInfo)


print("\nExercise 4")
#Write one function which will return the intersection of two sets passed in. 
#Write another function which will return the union of two sets passed in.

def setIntersection(set1, set2):
    return set1.intersection(set2)

def setUnion(set1, set2):
    return set1.union(set2)


print("\nExercise 5")
#Write a function that takes two lists of numbers, and returns the number that appears most frequently across both lists (the mode).
#Hint: if you get stuck, try creating a tally of how many times each number appears. This could be a list.

def findMostFrequent(list1, list2):
    combinedList = list1 + list2  
    return max(combinedList, key=combinedList.count)



print("\nExercise 6")
#Return to your student class created in Python 03 notebook. Create three new student objects and add/store these objects in a list.

class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def print(self):
        print(self.name)
        print(self.id)


student1 = Student("Kristiyan", "123")
student2 = Student("Grace", "456")
student3 = Student("Faisal", "789")

students = [student1, student2, student3]

for student in students:
    student.print()

print("\nExercise 7")
#Amend your Module class from Python 03 notebook so that module objects can store a list of student objects (which take the module). 
#Start by defining an attribute in the Module constructor. This could be initialised as an empty list in the constructor. 
#Create a add_student() function which can append a student object.

#Extension: is it possible to use the add_student() function to add a list of students to already existing list attribute?

class Module:
    def __init__(self, moduleName, moduleCode):
        self.moduleName = moduleName
        self.moduleCode = moduleCode
        self.students = []
        
    def addStudent(self, student):
        
            if isinstance(student, list):
                self.students.extend(student)  
            else:
                self.students.append(student) 
    
    def printInfo(self):
            print(f"Module Name: {self.moduleName}, Module Code: {self.moduleCode}")
            print("Students Enrolled:")
            for student in self.students:
                print(f" - {student.name} (ID: {student.studentId})")


class Course:
    def __init__(self, courseName, courseCode):
        self.courseName = courseName
        self.courseCode = courseCode
        self.modules = []
        


    def addModule(self, module):
            self.modules.append(module)
            
    def printInfo(self):
        print(f"Course Name: {self.courseName}, Course Code: {self.courseCode}")
        print("Modules:")
        for module in self.modules:
            module.printInfo()
            

class Student:
    def __init__(self, name, studentId, course):
        self.name = name
        self.studentId = studentId
        self.course = course

    def printInfo(self):
        print(f"Name: {self.name}, ID: {self.studentId}")
        self.course.printInfo()
        
module1 = Module("Programming Concepts", "COM4008")
course = Course("Computer Games Development", "GG46")

course.addModule(module1)

student1 = Student("Kristiyan Ivanov", 123, course)
student2 = Student("Grace ///", 456, course)
student3 = Student("Faisal ///", 789, course)

module1.addStudent(student1)
module1.addStudent([student2, student3])

module1.printInfo()

print("\nExercise 7.5")
#Now modify the list of the students in Module, to a dictionary. 
#The dictionary should store the student object as the 'key' and the student mark for the module as the 'value'. 
#Test this new structure works by passing in students and their marks when you call add_student()

#Extension: Can you now create some descriptive statistics for each module: the maximum mark, minimum mark, and mean (average)?

class Module:
    def __init__(self, moduleName, moduleCode):
        self.moduleName = moduleName
        self.moduleCode = moduleCode
        self.studentMarks = {}  

    def addStudent(self, student, mark):
        self.studentMarks[student] = mark  

    def printInfo(self):
        print(f"Module Name: {self.moduleName}, Module Code: {self.moduleCode}")
        print("Students Enrolled and Marks:")
        for student, mark in self.studentMarks.items():
            print(f" - {student.name} (ID: {student.studentId}), Mark: {mark}")

    
    def getStatistics(self):
        if not self.studentMarks:
            print("No students enrolled yet.")
            return
        
        marks = list(self.studentMarks.values())
        maxMark = max(marks)
        minMark = min(marks)
        meanMark = sum(marks) / len(marks)

        print(f"Maximum Mark: {maxMark}")
        print(f"Minimum Mark: {minMark}")
        print(f"Mean Mark: {meanMark:.2f}")

class Course:
    def __init__(self, courseName, courseCode):
        self.courseName = courseName
        self.courseCode = courseCode
        self.modules = []

    def addModule(self, module):
        self.modules.append(module)

    def printInfo(self):
        print(f"Course Name: {self.courseName}, Course Code: {self.courseCode}")
        print("Modules:")
        for module in self.modules:
            module.printInfo()

class Student:
    def __init__(self, name, studentId, course):
        self.name = name
        self.studentId = studentId
        self.course = course

    def printInfo(self):
        print(f"Name: {self.name}, ID: {self.studentId}")
        self.course.printInfo()
        
module1 = Module("Programming Concepts", "COM4008")
course = Course("Computer Games Development", "GG46")

course.addModule(module1)

student1 = Student("Kristiyan Ivanov", 123, course)
student2 = Student("Grace ///", 456, course)
student3 = Student("Faisal ///", 789, course)

module1.addStudent(student1, 85)
module1.addStudent(student2, 72)
module1.addStudent(student3, 90)

module1.printInfo()

module1.getStatistics()

print("\nExercise 8")
#Make adjustments to the Course class from Python 03 Notebook to allow a Course to store a list of module objects. 
#Create additional module objects and output their details.

class Module:
    def __init__(self, moduleName, moduleCode):
        self.moduleName = moduleName
        self.moduleCode = moduleCode

    def printInfo(self):
        print(f"Module Name: {self.moduleName}, Module Code: {self.moduleCode}")
        
class Course:
    def __init__(self, courseName, courseCode):
        self.courseName = courseName
        self.courseCode = courseCode
        self.modules = []
        
    def addModule(self, module):
        self.modules.append(module)

    def printModules(self):
        print(f"Course Name: {self.courseName}, Course Code: {self.courseCode}")
        print("Modules in this course:")
        for module in self.modules:
            module.printInfo()
            
course = Course("Computer Games Development", "GG46")

module1 = Module("Programming Concepts", "COM4008")
module2 = Module("Math For Games", "COM4009")
module3 = Module("Level Design", "COM4010")

course.addModule(module1)
course.addModule(module2)
course.addModule(module3)

course.printModules()

print("\nExercise 9")
#Write a function that will generate the multiplications of a number passed in. 
#For example, if the value 5 is passed in, then generate the 5 times table. 
#The values of the multiplication table should be stored in indivdiual elements (max 12) of a list. 
#The list should be returned at the end of the function.

def genMultiplicationTable(num):
    return [num * i for i in range(1, 13)]

table = genMultiplicationTable(int(input("Enter number: ")))
print("Multiplication Table:", table)


print("\nExercise 10")
#Write a function which will square any list of values passed into it. 
#Test this works by passing in your list of numbers (1-10) you created in the first exericse.

#Extension: what happens if the values in a list are not ints or floats? How would you respond to this event?

def squareValues(values):
    squared = []
    for value in values:
        if isinstance(value, (int, float)):
            squared.append(value ** 2)
        else:
            print(f"Invalid input: '{value}' is not a number.")
    return squared


numbers = list(range(1, 11))
squaredNumbers = squareValues(numbers)

print("Squared Values:", squaredNumbers)


print("\nExercise 11")
#You are given a list of integers, and your task is to find the longest subsequence of consecutive integers within the list. 
#A subsequence is a sequence that can be derived from another sequence by deleting some or no elements 
#without changing the order of the remaining elements.

#Write a Python function to solve this problem. 
#Your function should return the longest consecutive subsequence found in the original list.

#For example, given the input list:  [4, 2, 8, 5, 6, 7, 11, 12, 10]

#The longest consecutive subsequence is: [4, 5, 6, 7, 8]


def longestConsecutiveSubsequence(nums):
    if not nums:
        return []

    nums.sort() 
    longestSubseq = []
    currentSubseq = []

    for i in range(len(nums)):
        if i == 0 or nums[i] == nums[i - 1] + 1: 
            currentSubseq.append(nums[i])
        elif nums[i] != nums[i - 1]:  
            if len(currentSubseq) > len(longestSubseq):
                longestSubseq = currentSubseq
            currentSubseq = [nums[i]]  

 
    if len(currentSubseq) > len(longestSubseq):
        longestSubseq = currentSubseq

    return longestSubseq


inputList = [2, 2, 1, 5, 12, 3, 5, 4, 4, 6, 7, 11, 12, 10]
result = longestConsecutiveSubsequence(inputList)
print("Longest Consecutive Subsequence:", result)