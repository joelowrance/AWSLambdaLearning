import json
from FeedStorage import FeedStorage
from Config import Config

feed = FeedStorage(config=Config())


def get(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps(feed.get_feeds())
    }


print(get(123, 123))
