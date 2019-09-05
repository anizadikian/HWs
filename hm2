class Student:
    Assigment = 0.3
    Attendance = 0.1
    Quiz = 0.2
    Finalproject = 0.4

    def __init__(self, ID, firstName, lastName, phone, gender, birthdate, assigment, attendance, quiz, finalproject):
        self.ID = ID
        self.fname = firstName
        self.lname = lastName
        self.email = firstName + "." + lastName + "aua.am"
        self.phone = phone
        self.gender = gender
        self.birthdate = birthdate
        self.assigment = assigment
        self.attendance = attendance
        self.quiz = quiz
        self.finalproject = finalproject

    def getPersonalInfo(self):
        print(self.ID)
        print(self.fname)
        print(self.lname)
        print(self.email)
        print(self.phone)
        print(self.gender)
        print(self.birthdate)
        print("..................")

    def getCurrentGrade(self):
        finalassigment = self.assigment*self.Assigment
        finalattendance = self.attendance*self.Attendance
        finalquiz = self.quiz*self.Quiz
        fproject = self.finalproject*self.Finalproject
        print("Final grade:", finalassigment + finalattendance + finalquiz + fproject)
        print(".....................")

def main():
    st1 = Student("AUA123", "Ani", "Zadikian", "12345", "F", "23/04/99", 90, 50, 80, 70)
    st2 = Student("AUA345", "Gor", "Isoyan", "123455", "M", "01/05/99", 40, 50, 50, 70)

    st1.getPersonalInfo()
    st1.getCurrentGrade()


    st2.getPersonalInfo()
    st2.getCurrentGrade()


main()
