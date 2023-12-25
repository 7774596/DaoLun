import requests
import json


def get_followers(username, token):
    url = f"https://api.github.com/users/{username}/following"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        followers = response.json()
        return [follower["login"] for follower in followers]
    else:
        print("Error retrieving followers:", response.text)
        return []


def get_user_repos(username, token):
    url = f"https://api.github.com/users/{username}/repos"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        repos = response.json()
        return [repo["name"] for repo in repos]
    else:
        print(f"Error retrieving repositories for user {username}:", response.text)
        return []


def save_data_to_file(data, filename):
    with open(filename, "w") as file:
        json.dump(data, file)


username = "7774596"
token = "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"

followers = get_followers(username, token)

repo_data = {}
for follower in followers:
    repos = get_user_repos(follower, token)
    repo_data[follower] = repos

save_data_to_file(repo_data, "repo_data.json")