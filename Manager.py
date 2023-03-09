
from Deadline import Deadline
from Task import Task
from Note import Note

class TaskManager(Deadline, Note):
    def __init__(self):
        self.task_storage = {}
        self.last_id = 1

    def new_task(self):
        name = input("Введите имя задачи >>> ")
        author = input("Введите автора задачи >>> ")
        priority = int(input("Задайте приоритет >>> "))
        deadline = int(input("Определите кол-во дней на выполнение? >>> "))
        description = input("Описание задачи >>> ")
        new = Task(self.last_id, name, author, description, priority, self.deadline(deadline))
        self.task_storage[self.last_id] = new
        self.last_id += 1
        self.log(new.info())
        print(self.last_id)

    def show_tasks(self):
        print(self.task_storage)
        print(self.last_id)
        for i in sorted(self.task_storage, key = lambda x: self.task_storage[x].priority):
            print(self.task_storage[i].info())

    def show_log(self):
        with open('log.txt', 'r', encoding = 'utf-8') as file:
            print(file.read())
