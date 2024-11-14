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

    with open('{}.csv'.format(user_id), 'w+') as file:
        for todo in request:
            info = '"{}","{}","{}","{}"\n'.format(
                user_id, name, todo.get('completed'), todo.get('title'))
            file.write(info)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        employee_todo()
