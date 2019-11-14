class Node:
    def __init__(self, name=None ):
        self.name=name
        self.right=None
        self.left = None

class student:
    def __init__(self):
        self.student=None

    def __str__(self):
        if self.student == None:
            print("Root is Empty")
        else:
            return str(self.student.name)

    def addName(self,student_name):
        self.student=Node(student_name)

    def addCourse(self,course_name):
        if self.student.left==None:
            self.student.left=Node(course_name)
            return course_name
        if self.student.right == None:
            self.student.right = Node(course_name)

    def addAssignment(self,course,aname):
        pass

    def addGrade(self,assignment,grade):
        pass

    def printStudentinfo(self,name):
        if name != None:
            print(name.name, end=" ")
            self.printStudentinfo(name.right)
            self.printStudentinfo(name.left)
def main():
    student=student()
    student.addName("Ani")
    student.addCourse("ENGS103")
    student.addCourse("ENGS123")
    student.printStudentinfo(student1.student)
    
main()
