import logging

from process_controller import ProcessController
from task import tasks1, tasks2

logging.basicConfig(level=logging.DEBUG)


def main():
    pc = ProcessController()

    pc.set_max_proc(2)
    pc.start(tasks1, 3)
    logging.debug(f" - Currently {pc.alive_count()} processes are alive")
    logging.debug(" - Adding external tasks...")
    logging.debug(f" - Currently {pc.wait_count()} tasks left")
    pc.start(tasks2, 3)
    logging.debug(f" - Currently {pc.alive_count()} processes are alive")
    logging.debug(f" - Currently {pc.wait_count()} tasks left")
    pc.wait()
    logging.debug(" - All tasks completed.")


if __name__ == "__main__":
    main()
