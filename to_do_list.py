import pandas as pd
import os

class To_do_list():
    def __init__(self, filename="todo_list.csv"):
        self.filename = filename
        if os.path.exists(self.filename):
            self.tasks = pd.read_csv(self.filename)
        else:
            self.tasks = pd.DataFrame(columns=["task", "deadline"])

    def save_tasks(self):
        self.tasks.to_csv(self.filename, index=False)

    def select_menu(self):
        print('\n' * 2)
        print('----To-Do List Application----')
        print(' 1. Add Task')
        print(' 2. Remove Task')
        print(' 3. View Tasks')
        print(' 4. Exit')
        print('-------------------------------')

        selected_menu = int(input('Enter your choice (1 - 4): '))
        return selected_menu

    def add_task(self):
        task = input("\nEnter the task: ")
        deadline = input("Enter the deadline (optional, press enter to skip) e.g. 2025-12-31: ")
        if deadline:
            deadline = pd.to_datetime(deadline).date()
            new_task = pd.DataFrame({"task": [task], "deadline": [deadline]})
        else:
            new_task = pd.DataFrame({"task": [task]})
        self.tasks = pd.concat([self.tasks, new_task], ignore_index=True)
        print(f"    📋 '{task}' has been added.")
        self.save_tasks()

    def remove_task(self):
        task_no = input("\nEnter the task number to remove: ")

        if not task_no.isdigit():
            print("    ⚠️ Please enter a valid number.")
            return

        task_no = int(task_no)

        if 0 <= task_no < len(self.tasks):
            # Adjust for zero-based index
            removed_task = self.tasks.loc[task_no - 1, "task"]
            self.tasks = self.tasks.drop(task_no - 1).reset_index(drop=True)
            print(f"    ✂️ '{removed_task}' has been removed.")
            self.save_tasks()
        else:
            print(f"    ❌ Task {task_no} not found.")

    def view_tasks(self):
        if self.tasks.empty:
            print("    🗒️ The to-do list is empty.")
        else:
            print("\n📂 To-Do List:")
            for index, row in self.tasks.iterrows():
                task = row["task"]
                deadline = row["deadline"]
                print(f"{index + 1}. {task}")
                if not pd.isna(deadline):
                    print(f"   📅 Deadline: {deadline}")

    def exit_app(self):
        return print('\n👋 Exiting the application. Goodbye!')
