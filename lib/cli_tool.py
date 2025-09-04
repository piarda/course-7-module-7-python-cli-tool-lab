import argparse
from lib.models import Task, User

# Global dictionary to store users and their tasks
users = {}

alice = User("Alice")
unit_test_task = Task("Write unit tests")
alice.add_task(unit_test_task)
users["Alice"] = alice

def add_task(args):
    user = users.get(args.user)
    if not user:
        user = User(args.user)
        users[args.user] = user
    task = Task(args.title)
    user.add_task(task)

def complete_task(args):
    user = users.get(args.user)
    if not user:
        print(f"❌ User '{args.user}' not found.")
        return
    task = user.get_task_by_title(args.title)
    if not task:
        print(f"❌ Task '{args.title}' not found for user '{args.user}'.")
        return
    task.complete()

# CLI entry point
def main():
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    subparsers = parser.add_subparsers()

    # Subparser for adding tasks
    add_parser = subparsers.add_parser("add-task", help="Add a task for a user")
    add_parser.add_argument("user")
    add_parser.add_argument("title")
    add_parser.set_defaults(func=add_task)

    # Subparser for completing tasks
    complete_parser = subparsers.add_parser("complete-task", help="Complete a user's task")
    complete_parser.add_argument("user")
    complete_parser.add_argument("title")
    complete_parser.set_defaults(func=complete_task)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
