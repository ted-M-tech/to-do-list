from to_do_list import To_do_list

to_do_list_obj = To_do_list()

while True:
    selected_menu = to_do_list_obj.select_menu()
    if selected_menu == 1:
        to_do_list_obj.add_task()
    elif selected_menu == 2:
        to_do_list_obj.remove_task()
    elif selected_menu == 3:
        to_do_list_obj.view_tasks()
    elif selected_menu == 4:
        to_do_list_obj.exit_app()
        break
    else:
        print("Invalid choice. Please try again.")

