#!/usr/bin/python3
'''
Using what you did in the task #0, extend your
Python script to export data in the JSON format.
'''

if __name__ == '__main__':
    import json
    import requests
    import sys

    origin = "https://jsonplaceholder.typicode.com/"
    path = "users?_embed=todos"
    url = "{}{}".format(origin, path)

    resp = requests.get(url)
    json_resp = resp.text
    dict_resp = json.loads(json_resp)

    new_record = {}
    for record in dict_resp:
        id = '{}'.format(record.get('id'))
        username = record.get('username')
        todos = record.get('todos')
        new_record[id] = []

        for task in todos:
            task_title = task.get('title')
            task_status = task.get('completed')
            dict_obj = {
                'username': username,
                'task': task_title,
                'completed': task_status
            }
            new_record[id].append(dict_obj)

    with open('todo_all_employees.json', 'w') as f:
        json.dump(new_record, f)
