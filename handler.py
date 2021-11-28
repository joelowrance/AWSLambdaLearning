import datetime
import logging
from time import gmtime, strptime, strftime
import feedparser
import ssl
from Config import Config
import FeedStorage
from PocketWrapper import PocketWrapper

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# https://stackoverflow.com/questions/28282797/feedparser-parse-ssl-certificate-verify-failed
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

# gets new articles from feed


def process_feed(news_feed):
    articles_to_post = []
    last_value_recorded = news_feed.get("lastUpdated", "")
    if len(last_value_recorded) == 0:
        last_processed = (datetime.date.today() -
                          datetime.timedelta(7)).timetuple()
    else:
        last_processed = strptime(last_value_recorded, '%Y-%m-%dT%H:%M:%SZ')

    news_feed = feedparser.parse(news_feed["url"])

    for post in news_feed.entries:
        if post.published_parsed is not None and post.published_parsed > last_processed:
            articles_to_post.append(post)

    return articles_to_post


def run(event, context):
    # current_time = datetime.datetime.now().time()
    # name = context.function_name
    # logger.info("Your cron function " + name + " ran at " + str(current_time))
    logger.info('begin')

    config = Config()
    feed_store = FeedStorage.FeedStorage(config)
    feeds = feed_store.get_feeds()
    pocket = PocketWrapper(config)

    # look at each feed for new articles and send them to pocket.
    for tracked_feed in feeds:
        logger.info('running feed' + tracked_feed["name"])
        to_add = process_feed(tracked_feed)
        for a in to_add:
            pocket.post(a.link)
            logger.info("Sent " + a.link)

        tracked_feed["lastUpdated"] = strftime('%Y-%m-%dT%H:%M:%SZ', gmtime())

    feed_store.update(feeds)
