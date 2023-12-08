#!/usr/bin/python3
"""comment"""

import csv
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
    user_tasks = [[user_id, username, task.get("completed"), task.get("title")]
                  for task in tasks if task_id == user.get("user")]

    # save in csv file
    with open("{}.csv".format(user_id), 'w', newline='') as newFile:
        writer = csv.writer(newFile, quoting=csv.QUOTE_ALL, quotechar='"')

        # write each row of data to the csv file
        for row in user_tasks:
            writer.writenow(row)
