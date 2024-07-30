#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to JSON format.
"""
import json
import requests
import sys


def export_to_json():
    userId = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    user_url = '{}/users/{}'.format(url, userId)
    user = requests.get(user_url).json()
    todo_url = '{}/todos?userId={}'.format(url, userId)
    todo = requests.get(todo_url).json()
    name = user.get('username')

    userTodo = {}
    taskList = []

    for task in todo:
        taskDict = {"task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": name}
        taskList.append(taskDict)
    userTodo[userId] = taskList

    filename = userId + '.json'
    with open(filename, 'w') as fjs:
        json.dump(userTodo, fjs)

    # user_id = sys.argv[1]
    # url = "https://jsonplaceholder.typicode.com/"
    # user = requests.get(url + "users/{user_id}").json()
    # username = user.get("username")
    # todos = requests.get(url + "todos", params={"userId": user_id}).json()

    # with open("{}.json".format(user_id), "w") as jsonfile:
    #     json.dump({user_id: [{
    #             "task": t.get("title"),
    #             "completed": t.get("completed"),
    #             "username": username
    #         } for t in todos]}, jsonfile)


if __name__ == "__main__":
    export_to_json()
