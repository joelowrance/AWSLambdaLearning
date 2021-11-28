import json
import boto3
import Config
import logging


class FeedStorage:
    session: boto3.session

    def __init__(self, config: Config):
        self.config = config

    def get_feeds(self):
        s3_client = boto3.client('s3', aws_access_key_id=self.config.aws_key_id,
                                 aws_secret_access_key=self.config.secret_aws_access_key)
        response = s3_client.get_object(
            Bucket=self.config.aws_bucket, Key=self.config.aws_file_name)
        content = response['Body'].read().decode('utf-8')
        return json.loads(content)

    def update(self, json_data):
        logging.info("updating feed")
        logging.info(json.dumps(json_data).encode('UTF-8'))
        s3 = boto3.resource('s3', aws_access_key_id=self.config.aws_key_id,
                            aws_secret_access_key=self.config.secret_aws_access_key)
        s3object = s3.Object(self.config.aws_bucket, self.config.aws_file_name)
        s3object.put(
            Body=(bytes(json.dumps(json_data).encode('UTF-8')))
        )
