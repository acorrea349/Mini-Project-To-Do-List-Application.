
# Create a command-line interface (CLI) for the To-Do List Application.
# Display a welcoming message and a menu with the following options:
#         Welcome to the To-Do List App!

#         Menu:
#         1. Add a task
#         2. View tasks
#         3. Mark a task as complete
#         4. Delete a task
#         5. Quit

def main_menu():
    print("Welcome to the To-Do-List Application!")
    print("   Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task complete")
    print("4. Delete a task")
    print("5. Quit")

print(main_menu())



to_do_list = ["eat","wash","clean","shower","work","excercise"]



def main():

    try:
        user_input = int(input("""
What option from the Menu would you like to choose (Please input your option in a numeric value.): """))
        
    except ValueError:
        print("Entry not valid. Please input a digit 1-5 from the Menu option.")

    else:
        while True:
        
            if user_input == 1:
                print("Add a task")
                to_do_list.append(input("Enter the task would you like to add to your To-Do-List: ").upper())
                another_task = input("Would you like to add another task? (yes/ no) ")
                if another_task == "yes".lower():
                    for list in to_do_list: 
                        print(f"Incomplete task: ->{list}.")
                else: 
                    for list in to_do_list:
                        print(f"Incomplete task: ->{list}.")
                    break                        

            elif user_input == 2:
                print("View tasks:")
                for list in to_do_list:
                    print(f"->{list}")
                break

            elif user_input == 3:
                completed_task = input("What task would you like to mark as complete: ")
                if completed_task in to_do_list:
                    print(f"Completed Task: {completed_task}")
                    break
                else:
                    print("Task not in list")
                    break

            elif user_input == 4:
                delete_task = input("What task would you like to delete: ").lower()
                if delete_task in to_do_list:
                    to_do_list.remove(delete_task)
                    print(f"Updated list: {to_do_list}")
                    break
                else:
                    print("Task not in list")
                    break

            elif user_input == 5:
                print("Quit")
                break

            else:
                print("Entry not in Menu (1-5)")
                break

    finally:
        print("Thank you for using the To Do List App.")


main()
