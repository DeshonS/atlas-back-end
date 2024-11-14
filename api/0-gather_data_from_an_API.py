#!/usr/bin/python3
"""Employee Task API"""
import requests
import sys


def employee_todo():
    user_id = sys.argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    todo = 'https://jsonplaceholder.typicode.com/todos/?userId={}'.format(
        user_id)
    name = requests.get(user_url).json().get('name')
    request = requests.get(todo).json()
    tasks = [task.get('title') for task in request if task.get('completed')
             is True]
    print('Employee {} is done with tasks({}/{}):'.
          format(name, len(tasks), len(request)))
    print('\n'.join('\t {}'.format(task) for task in tasks))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        employee_todo()
