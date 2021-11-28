import json


class Config:
    def __init__(self):
        with open('config.json') as configFile:
            jsdoc = json.load(configFile)
            self.pocket_consumer_key = jsdoc["pocket"]["consumer_key"]
            self.pocket_access_token = jsdoc["pocket"]["access_token"]
            self.aws_key_id = jsdoc["aws"]["access_key_id"]
            self.secret_aws_access_key = jsdoc["aws"]["secret_access_key"]
            self.aws_bucket = jsdoc["aws"]["s3_bucket"]
            self.aws_file_name = jsdoc["aws"]["file_name"]
