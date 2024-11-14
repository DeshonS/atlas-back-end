#!/usr/bin/python3
"""Employee ID API"""
import requests
import sys


def emp_todo(employee_id):
    uurl = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)
    turl = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id)
    user_response = requests.get(uurl)
    user_data = user_response.json()
    employee_name = user_data.get("name")
    td_response = requests.get(turl)
    tdata = td_response.json

    total_tasks = len(tdata)
    completed_tasks = [task for task in tdata if
                       task["completed"]]
    number_of_finished_tasks = len(completed_tasks)
    print("Employee {} is done with tasks({}/{}):".format(
        number_of_finished_tasks, total_tasks))
    for task in completed_tasks:
        print("\t {}".format({task['title']}))

    if __name__ == "__main__":
        emp_todo(employee_id)
