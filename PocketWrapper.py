from pocket import Pocket, PocketException
import Config


class PocketWrapper:
    def __init__(self, config: Config):
        self.pocket_api = Pocket(
            consumer_key=config.pocket_consumer_key,
            access_token=config.pocket_access_token
        )

    def post(self, url):
        self.pocket_api.add(url)
