#!/usr/bin/python3
"""comment"""

import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_id = int(sys.argv[1])
    user_endpoint = "{}/user/{}".format(url, user_id)
    username = requests.get(user_endpoint).json().get("username")
    tasks_endpoint = "{}/todos".format(url)
    tasks = requests.get(tasks_endpoint).json()
    user_tasks = {USER_ID: [{"task": task.get("title"),
                            "completed": task.get("completed"),
                             "username": username}
                  for task in tasks if tasks.get("userId") == user_id]}

    # save in json file
    with open("{}.json".format(user_id), 'w', encoding="utf-8") as newFile:
        json.dump(user_tasks, newFile)
