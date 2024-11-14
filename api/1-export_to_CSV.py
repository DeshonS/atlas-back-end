#!/usr/bin/python3
"""Employee ID API"""
import requests
import sys
import csv


def emp_todo(employee_id):
    uurl = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)
    turl = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id)
    user_response = requests.get(uurl)
    user_data = user_response.json()
    employee_name = user_data['username']
    td_response = requests.get(turl)
    tdata = td_response.json()

    total_tasks = len(tdata)
    completed_tasks = [task for task in tdata if
                       task["completed"]]
    number_of_finished_tasks = len(completed_tasks)
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_finished_tasks, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task['title']))
    filename = f"{employee_id}.csv"
    with open(filename, mode="w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in tdata:
            writer.writerow([employee_id, employee_name, task["completed"], task["title"]])


if __name__ == "__main__":
    employee_id = sys.argv[1]
    emp_todo(employee_id)
