#!/usr/bin/python3
""" Python script that uses a REST API, for a given employee ID,
& returns information about his/her TODO list progress"""
if __name__ == "__main__":

    import requests
    import sys

    API = "https://jsonplaceholder.typicode.com"

    if len(sys.argv) > 1:
        userId = sys.argv[1]
        user = requests.get('{}/users/{}'.format(API, userId)).json()
        userName = user.get('name')
        userTodo = requests.get('{}/todos'.format(API)).json()
        totalTasks = 0
        completed = 0

        for task in userTodo:
            if task.get('userId') == int(userId):
                totalTasks += 1
                if task.get('completed'):
                    completed += 1

        print('Employee {} is done with tasks({}/{}):'
              .format(userName, completed, totalTasks))

        print('\n'.join(["\t " + task.get('title') for task in userTodo
              if task.get('userId') == int(userId) and task.get('completed')]))
