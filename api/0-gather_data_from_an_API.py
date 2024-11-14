#!/usr/bin/python3
"""Employee Task API"""
import requests
import sys


def get_employee_todo_progress(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id)

    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Employee not found.")
        return
    user_data = user_response.json()
    employee_name = user_data.get("name")

    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Could not retrieve TODO list.")
        return
    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    completed_tasks = [task for task in todos_data if task.get("completed")]
    num_completed_tasks = len(completed_tasks)

    print(f"Employee {employee_name} is done with 
          tasks({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Please provide a valid employee ID (integer).")
