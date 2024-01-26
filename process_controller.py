import logging
import multiprocessing
import threading
import time


class ProcessController:
    def __init__(self):
        self.max_proc = 1
        self.threads = []
        self.tasks_left = 0

    def set_max_proc(self, n):
        self.max_proc = n

    def start(self, tasks: list, max_exec_time):
        self.tasks_left += len(tasks)
        for task in tasks:
            while sum(1 for thread in self.threads if thread.is_alive()) >= self.max_proc:
                time.sleep(0.1)
            func, args = task
            process_thread = threading.Thread(target=self._run_process, args=(func, args, max_exec_time))
            process_thread.start()
            self.threads.append(process_thread)

    def _run_process(self,  func, args, max_exec_time):
        process = multiprocessing.Process(target=func, args=args)
        process.start()
        self.tasks_left -= 1
        process.join(max_exec_time + 0.1)

        if process.is_alive():
            logging.debug(f" < {args[0]} terminated")
            process.terminate()

    def wait(self):
        for process_thread in self.threads:
            process_thread.join()

    def wait_count(self):
        return self.tasks_left

    def alive_count(self):
        return sum(1 for p in self.threads if p.is_alive())
