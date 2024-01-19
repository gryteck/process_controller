from process_controller import ProcessController
from task import tasks


def main():
    pc = ProcessController()

    pc.set_max_proc(2)
    pc.start(tasks, 4)

    print("Waiting for tasks to finish...")

    pc.wait()

    print("All tasks completed.")
    print(f"- {pc.wait_count()} tasks left")


if __name__ == "__main__":
    main()
