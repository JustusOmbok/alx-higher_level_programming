#!/usr/bin/python3
""" Python script that takes 2 arguments """
import requests
import sys

if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repository_name}/commits"

    try:
        response = requests.get(url)
        commits = response.json()

        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")

    except ValueError:
        print("An error occurred while fetching data from the GitHub API.")
