import requests
from .base import Provider


class GithubReleaseProvider(Provider):

    def __init__(self, repository):
        self.repository = repository


    def get_state(self):

        url = f"https://api.github.com/repos/{self.repository}/releases"

        print("Requesting:", url)

        response = requests.get(url)

        print("Status code:", response.status_code)

        response.raise_for_status()

        releases = response.json()

        print("Number of releases found:", len(releases))

        if not releases:
            print("No releases found")
            return {}

        return {
            release["id"]: {
                "name": release["name"],
                "url": release["html_url"]
            }
            for release in releases
        }