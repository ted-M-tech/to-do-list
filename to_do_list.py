import pandas as pd
import os

class To_do_list():
    def __init__(self):
        pass

    def load_file(self):
        # Read to do list csv file
        if os.path.exists('to_do_list.csv'):
            to_do_list = pd.read_csv('to_do_list.csv')
        else:
            to_do_list = pd.DataFrame(columns=['Tasks'])
            to_do_list.to_csv('to_do_list.csv', index=False)
        return to_do_list

    def select_menu(self):
        print("\nTo-do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Exit")
        selected_menu = input("Enter your choice: ")
        print("")
        return selected_menu

    def add_task(self):
        task = input("Enter the task: ")
        df_task = pd.DataFrame({'Tasks': [task]})
        df_task.to_csv('to_do_list.csv', mode='a', header=False, index=False)
        return print(f"'{task}' has been added to the list.")

    def remove_task(self):
        delete_task = input("Enter the task to remove: ")
        to_do_list = pd.read_csv('to_do_list.csv')
        to_do_list = to_do_list[to_do_list['Tasks'] != delete_task]
        to_do_list.to_csv('to_do_list.csv', index=False)
        return print(f"'{delete_task}' has been removed from the list.")

    def view_tasks(self):
        to_do_list = pd.read_csv('to_do_list.csv')
        print("To-do List:")
        for index, task in enumerate(to_do_list['Tasks'], start=1):
            print(f"{index}. {task}")

    def exit_app(self):
        return print("Exiting the application. Goodbye!")
