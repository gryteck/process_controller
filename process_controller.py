import time
import multiprocessing


def task_wrapper(task: tuple, max_exec_time: int) -> None:
    func, args = task
    start_time = time.time()
    while time.time() - start_time < max_exec_time:
        func(*args)
        break


class ProcessController:
    max_proc: int
    processes: list[multiprocessing.Process]

    def __init__(self, max_proc: int = 1):
        self.max_proc = max_proc
        self.processes = []
        self.tasks = []
        self.queue = multiprocessing.Queue()

    def set_max_proc(self, n: int) -> None:
        self.max_proc = n

    def start(self, tasks: list[tuple], max_exec_time: int) -> None:
        for task in tasks:
            self.queue.put(task)
        while not self.queue.empty():
            task = self.queue.get()
            while self.alive_count() >= self.max_proc:
                time.sleep(0.1)
            process = multiprocessing.Process(target=task_wrapper, args=(task, max_exec_time))
            self.processes.append(process)
            process.start()

    def wait(self) -> None:
        for process in self.processes:
            process.join()

    def wait_count(self) -> int:
        # Raises NotImplementedError on Mac OSX because of broken sem_getvalue()
        return self.queue.qsize()

    def alive_count(self) -> int:
        return sum(1 for p in self.processes if p.is_alive())
