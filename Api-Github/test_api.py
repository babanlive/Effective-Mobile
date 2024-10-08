import os

import requests

from dotenv import load_dotenv


load_dotenv()

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("REPO_NAME")
BASE_URL = os.getenv("BASE_URL")


if not all([GITHUB_USERNAME, GITHUB_TOKEN, REPO_NAME, BASE_URL]):
    raise ValueError("One or more variables are not defined. Check your .env file.")

HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}


def main() -> None:
    try:
        create_repo(REPO_NAME)

        if check_repo_exists(REPO_NAME):
            print(f"2. Repository '{REPO_NAME}' exists.")
        else:
            print(f"2. Error creating repository '{REPO_NAME}'.")

        delete_repo(REPO_NAME)

    except requests.exceptions.RequestException as e:
        print(f"HTTP request error: {e}")
    except Exception as ex:
        print(f"An error occurred: {ex}")


def create_repo(repo_name: str) -> None:
    url: str = f"{BASE_URL}/user/repos"
    data = {
        "name": repo_name,
        "description": "Test repository",
        "auto_init": True,
        "private": False,
    }
    response = requests.post(url, headers=HEADERS, json=data)

    if response.status_code == 201:
        print(f"1. Created repository '{repo_name}'.")
    elif response.status_code == 422:
        print(f"1. Repository '{repo_name}' already exists.")
    else:
        response.raise_for_status()


def check_repo_exists(repo_name: str) -> bool:
    url: str = f"{BASE_URL}/repos/{GITHUB_USERNAME}/{repo_name}"
    response: requests.Response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return True
    elif response.status_code == 404:
        return False
    else:
        response.raise_for_status()


def delete_repo(repo_name: str) -> None:
    url: str = f"{BASE_URL}/repos/{GITHUB_USERNAME}/{repo_name}"
    response: requests.Response = requests.delete(url, headers=HEADERS)

    if response.status_code == 204:
        print(f"Repository '{repo_name}' has been deleted.")
    elif response.status_code == 404:
        print(f"Repository '{repo_name}' not found.")
    else:
        response.raise_for_status()


if __name__ == "__main__":
    main()
