import time


def example_task(message: str, sleep_time: int):
    print(message+' started')
    time.sleep(sleep_time)
    print(message+' finished')


tasks = [
        (example_task, ("Task 1", 4)),
        (example_task, ("Task 2", 3)),
        (example_task, ("Task 3", 1)),
        (example_task, ("Task 4", 4))
    ]
