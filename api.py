import json
from FeedStorage import FeedStorage
from Config import Config

feed = FeedStorage(config=Config())


def get(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps(feed.get_feeds())
    }


def update(event, context):
    data = json.loads(event["body"])
    feed.update(data)
    return {
        "statusCode": 200,
        "body": json.dumps(data)
    }
