import logging
import time


def example_task(message: str, sleep_time: int):
    logging.debug(" > " + message + ' started')
    time.sleep(sleep_time)
    logging.debug(" < " + message + ' finished')


tasks1 = [
    (example_task, ("Task 1", 4)),
    (example_task, ("Task 2", 3)),
    (example_task, ("Task 3", 1)),
    (example_task, ("Task 4", 4))
]

tasks2 = [
    (example_task, ("Task 5", 7)),
    (example_task, ("Task 6", 2)),
    (example_task, ("Task 7", 3)),
    (example_task, ("Task 8", 9))
]
