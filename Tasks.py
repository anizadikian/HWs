class Task:
    def __init__(self, name, deadline, priority):
        self.name = name
        self.deadline = deadline
        self.priority = priority

class TaskManager:
    def __init__(self):
        self.task = []

    def addTask(self, task):
        self.task.append(task)

    def printTheMostImportantTask(self):
        for task in self.task:
            for i in range(10, 0, -1):
                print(task.name, task.deadline)
            else:
                 continue

    def printAllTasks(self):
        print("All Tasks : ")
        print(self.task)

def main():

    auaTasks=TaskManager()
    personalTask=TaskManager()

    t=Task("Calculus HW","10/10/19", 8)
    auaTasks.addTask(t)

    t=Task("Get Ready For Midterms", "26/10/19" , 5)
    auaTasks.addTask(t)

    t=Task("Pay Cellphone Bill" , "22/10/19" , 2)
    personalTask.addTask(t)

    t=Task("sister Birthday Gift", "22/10/19", 10)
    personalTask.addTask(t)

    auaTasks.printAllTasks()
    personalTask.printTheMostImportantTask()
main()
