import json
import sys
import FeedStorage
from Config import Config
import FeedStorage


config = Config()
feed_store = FeedStorage.FeedStorage(config)


def download():
    contents = feed_store.get_feeds()
    with open('feeds.json', 'w') as file:
        json.dump(contents, file)


def upload():
    with open('feeds.json') as file:
        contents = json.load(file)
        feed_store.update(contents)


print(__name__)
print(__file__)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        exit()

    op = str(sys.argv[1])
    if op == 'd':
        download()
    elif op == 'u':
        upload()
