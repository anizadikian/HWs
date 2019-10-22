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


        # def selectionSort(head):
        #
        #     a = b = head
        #
        #     while b.next:
        #
        #         c = d = b.next
        #         while d:
        #
        #             if b.data > d.data:
        #                 if b.next == d:
        #                     if b == head:
        #                         b.next = d.next
        #                         d.next = b
        #                         b, d = d, b
        #                         c = d
        #                         head = b
        #                         d = d.next
        #                     else:
        #                         b.next = d.next
        #                         d.next = b
        #                         a.next = d
        #
        #                         b, d = d, b
        #                         c = d
        #                         d = d.next
        #
        #                 else:
        #
        #
        #                     if b == head:
        #
        #                         r = b.next
        #                         b.next = d.next
        #                         d.next = r
        #                         c.next = b
        #
        #
        #                         b, d = d, b
        #                         c = d
        #
        #                         d = d.next
        #
        #                         head = b
        #
        #                     else:
        #
        #                         r = b.next
        #                         b.next = d.next
        #                         d.next = r
        #                         c.next = b
        #                         a.next = d
        #
        #                         b, d = d, b
        #                         c = d
        #                         d = d.next
        #
        #             else:
        #                 c = d
        #                 d = d.next
        #
        #         a = b
        #         b = b.next
        #
        #     return head

    # def printList(head):
    #
    #     while head:
    #         print(head.data, end=" ")
    #         head = head.next

def main():

    my_student = Students()

    my_student.setHead("Gor Isoyan", 3)

    my_student.append("Amaras Mehrabi", 4)
    my_student.append("Shantal Adajian", 4)
    my_student.append("Aspet Davoodi", 3)

    my_student.addAtBeginning("Ani Zadikian", 3)

    my_student.display()

    # head = selectionSort(head)
    # 
    # printList(head)

main()
