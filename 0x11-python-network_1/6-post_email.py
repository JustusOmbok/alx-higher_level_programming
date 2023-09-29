#!/usr/bin/python3
""" Python script that takes in a URL and an email address """
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    response = requests.post(url, data=payload)
    print(response.text)
