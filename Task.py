from Note import Note
from datetime import datetime


class Task(Note):
    def __init__(self, id, name, author, description, priority, deadline):
        self.id = id
        self.name = name
        self.author = author
        self.created = datetime.now()
        self.description = description
        self.priority = priority
        self.deadline = deadline

    def info(self):
        return f"Задача: {self.name}, id: {self.id}, автор: {self.author}, создана: {self.created.strftime('%d %b %Y, %H:%M:%S')},\
4 имеет приоритет: {self.priority}, время на выполнение: {self.deadline.strftime('%d %b %Y, %H:%M')}, \
 описание: {self.description}."