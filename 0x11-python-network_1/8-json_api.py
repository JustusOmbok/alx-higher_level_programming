#!/usr/bin/python3
""" Python script that takes in a letter and sends a POST request """
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        payload = {"q": ""}
    else:
        payload = {"q": sys.argv[1]}


    url = 'http://0.0.0.0:5000/search_user'
    response = requests.post(url, data=payload)

    try:
        data = response.json()

        if data:
            print("[{}] {}".format(data.get('id'), data.get('name')))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
