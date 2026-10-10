def show_menu():
    print("====== Todo App Menu ======")
    print("1. Add a new todo")
    print("2. List all todos")
    print("3. Mark a todo as done")
    print("4. Delete a todo")
    print("5. Exit")


def list_todos(todos):
    if not todos:
        print("No todos found.")
        return
    for todo in todos:
        status = "[🟢]" if todo['done'] else "[🔴]"
        print(f"{status} {todo['task']}")


def add_todo(todos):
    content = input("Enter the task:").strip()
    if not content:
        print("Task cannot be empty.")
        return
    todos.append({"No.": len(todos) + 1, "task": content, "done": False})
    print(f"Added todo: {content}")

def mark_todo(todos):
    if not todos:
        print("No todos found.")
        return
    num = int(input("Enter the number of the todo to mark as done:"))
    if num < 1 or num > len(todos):
        print("Invalid todo number.")
        return
    for todo in todos:
        if todo["No."] == num:
            todo["done"] = True
            print(f"Marked todo '{todo['task']}' as done.")
            return
        
def change_todo(todos):
    if not todos:
        print("No todos found.")
        return
    num = int(input("Enter the number of the todo to change:"))
    if num < 1 or num > len(todos):
        print("Invalid todo number.")
        return
    new_content = input("Enter the new task:").strip()
    if not new_content:
        print("Task cannot be empty.")
        return
    for todo in todos:
        if todo["No."] == num:
            todo["task"] = new_content
            print(f"Changed todo to '{new_content}'.")
            return