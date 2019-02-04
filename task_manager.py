import string
import threading


class TaskManager:
    def __init__(self):
        self.running_tasks = []

    def is_task_running(self, task_name: string):
        for name,is_running,task in self.running_tasks:
            if name == task_name:
                return is_running
        return False

    def run_task(self, task_name: string, task: threading.Thread):
        self.running_tasks.append((task_name, True, task))
        print("[MANAGER] Task started: %s" % task_name)
        task.start()

    def finish_task(self, task_name):
        for i, val in enumerate(self.running_tasks):
            name, is_running, task = val
            if name == task_name and is_running:
                self.running_tasks[i] = (name, False, task)
                task.join()
                print("[MANAGER] Finished task: %s" % name)

    def finish_all_task(self):
        for i, val in enumerate(self.running_tasks):
            name, is_running, task = val
            self.running_tasks[i] = (name, False, task)
            print("[MANAGER] Finished task: %s" % name)
