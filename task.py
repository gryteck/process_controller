import time

class Tasks:
    def __init__(self, tasks: list[tuple]):
        self.tasks = tasks

    def get(self) -> tuple:
        task = self.tasks[0]
        self.tasks.remove(task)
        return task

    def left(self):
        return len(self.tasks)


def example_task(message, sleep_time):
    print(message+' started')
    time.sleep(sleep_time)
    print(message+' finished')


tasks = [
        (example_task, ("Task 1", 4)),
        (example_task, ("Task 2", 3)),
        (example_task, ("Task 3", 1)),
        (example_task, ("Task 4", 4))
    ]
