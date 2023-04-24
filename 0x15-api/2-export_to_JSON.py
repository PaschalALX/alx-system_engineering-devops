#!/usr/bin/python3
'''
Using what you did in the task #0, extend your
Python script to export data in the JSON format.
'''

if __name__ == '__main__':
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
    username = dict_resp.get('username')
    todos = dict_resp.get('todos')

    records = []
    for task in todos:
        task_title = task.get('title')
        status = task.get('completed')
        dict_obj = {
            'task': task_title,
            'completed': status,
            'username': username
        }
        records.append(dict_obj)

    record_obj = {
        '{}'.format(user_id): records
    }

    with open('{}.json'.format(user_id), 'w') as f:
        json.dump(record_obj, f)
