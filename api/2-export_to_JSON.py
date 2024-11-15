#!/usr/bin/python3
"""Employee Task API"""
import json
import requests
import sys


def employee_todo():
    user_id = sys.argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    todo = 'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(
        user_id)
    name = requests.get(user_url).json().get('username')
    request = requests.get(todo).json()
    tasks = []

    with open('{}.json'.format(user_id), 'w+') as file:
        for todo in request:
            task = {"task": todo.get("title"),
                    "completed": todo.get("completed"), "username": name}
            tasks.append(task)
        info = {user_id: tasks}
        file.write(json.dumps(info))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        employee_todo()
