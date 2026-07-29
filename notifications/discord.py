import requests


class DiscordNotifier:

    def __init__(self, webhook):
        self.webhook = webhook


    def send(self, message):

        requests.post(
            self.webhook,
            json={
                "content": message
            }
        )