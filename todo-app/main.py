from todo import add_todo,list_todos,mark_todo,change_todo
from storage import load_todos, save_todos
from todo import show_menu

def main():
    todos = load_todos()
    while True:
        show_menu()
        choice = input("Enter your choice:").strip()
        if choice == "1":
            add_todo(todos)
        elif choice == "2":
            list_todos(todos)
        elif choice == "3":
            mark_todo(todos)
        elif choice == "4":
            change_todo(todos)
        elif choice == "5":
            save_todos(todos)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
