import sys

class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def complete(self):
        self.completed = True
        try:
            print(f"✅ Task '{self.title}' completed.")
        except UnicodeEncodeError:
            print(f"[OK] Task '{self.title}' completed.")


class User:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        try:
            print(f"📌 Task '{task.title}' added to {self.name}.")
        except UnicodeEncodeError:
            print(f"[+] Task '{task.title}' added to {self.name}.")

    def get_task_by_title(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None
