#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress.
"""
from sys import argv
import requests


def get_todo_list_progress():
    if len(argv) > 1:
        uid = argv[1]
        req_url = "https://jsonplaceholder.typicode.com/"
        users_req = requests.get(req_url + f"users/{uid}").json()
        todos_req = requests.get(req_url + f"todos",
                                 params={"userId": uid}).json()
        completed = [todo.get("title")
                     for todo in todos_req
                     if todo.get("completed") is True
                     ]
        print(
            f"Employee {users_req.get('name')} is done with tasks("
            f"{len(completed)}/{len(todos_req)}):"
        )
        [print(f"\t {c}") for c in completed]


if __name__ == "__main__":
    get_todo_list_progress()
