#!/usr/bin/python3
'''
Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress.
'''
import json
import requests
import sys

user_id = sys.argv[1]
origin = "https://jsonplaceholder.typicode.com/"
path = "users/{}?_embed=todos".format(user_id)
url = "{}{}".format(origin, path)

resp = requests.get(url)
json_resp = resp.text
dict_resp = json.loads(json_resp)
employee = dict_resp.get('name')
todos = dict_resp.get('todos')
todos_num = len(todos)
cmpd_tasks = [task for task in todos if task.get('completed')]
cmpd_tasks_num = len(cmpd_tasks)

temp = 'Employee {} is done with tasks({}/{}):'
text = temp.format(employee, cmpd_tasks_num, todos_num)

print(text)
for task in cmpd_tasks:
    print('\t {}'.format(task.get('title')))
