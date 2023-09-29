#!/usr/bin/python3
""" Python script that takes your GitHub credentials """
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    url = 'https://api.github.com/user'
    auth = (username, token)

    try:
        response = requests.get(url, auth=auth)
        data = response.json()

        if 'id' in data:
            print(data['id'])
        else:
            print("None")

    except ValueError:
        print("None")
