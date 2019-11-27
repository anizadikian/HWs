import os
import json

class Task:
    def __init__(self, name, deadline, time):
        self.name = name
        self.deadline = deadline
        self.time = time

class HashTable:
    def __init__(self):
        self.size = 0
        self.tasks = []
        self.table = []

    def LoadTasks(self):
        with open("data.json") as data:
            tasks = json.load(data)
            for key in tasks:
                tmptask= tasks(key, tasks[key])
                self.tasks.append(tmptask)
                self.size = self.size + 1

    def HashFunction(self, key):
        return key % self.size

    def Insert(self):
        self.table = [None] * self.size
        for task in self.tasks:
            number = 0
            for letter in task.name:
                number = (number + ord(letter))

            self.table[self.HashFunction(number)] = task

        print(self.table)

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def ascii(self, table):
        for name in range(table.size):
            key = table.users[name]
            ascii = 0
            for c in key:
                ascii = ord(c) + ascii
                table[ascii] = key
def main():
    
    table = HashTable()
    table.LoadTasks()
    table.Insert()

main()
