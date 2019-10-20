class Student:

    def __init__(self, name=None, gpa=None):
        self.name = name
        self.gpa = gpa
        self.next = None

class Students:

    def __init__(self):
        self.__head = None


    def setHead(self, student, gpa):
        self.__head = Student(student, gpa)

    def display(self):
        printval = self.__head
        while printval is not None:
            print(printval.name, printval.gpa)
            printval = printval.next

    def append(self, name, gpa):
        temp = self.__head
        while temp.next is not None:
            temp = temp.next

        student1 = Student(name, gpa)
        temp.next = student1

    def addAtBeginning(self, name, gpa):
        newstudent = Student(name, gpa)

        newstudent.next = self.__head
        self.__head = newstudent

    def printGPA(self, name, gpa):
        pass

def main():

    my_student = Students()

    my_student.setHead("Gor Isoyan", 3)

    my_student.append("Amaras Mehrabi", 4)
    my_student.append("Shantal Adajian", 4)
    my_student.append("Aspet Davoodi", 3)

    my_student.addAtBeginning("Ani Zadikian", 3)

    my_student.display()

main()
