#!/usr/bin/python3
"""comment"""

import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_endpoint = "{}/user".format(url)
    username = requests.get(user_endpoint).json()
    tasks_endpoint = "{}/todos".format(url)
    tasks = requests.get(tasks_endpoint).json()
    user_tasks = {user.get("id"): [{"username": user.get("username"),
                                    "task": task.get("title"),
                                    "completed": task.get("completed"),
                  for task in tasks if task.get("userId") == user.get("id")]
                  for user in users}

    print(user_tasks)

    # save in json file
    with open("todo_all_employees.json", 'w', encoding="utf8") as opeded_file:
        json.dump(user_tasks, opened_file)
