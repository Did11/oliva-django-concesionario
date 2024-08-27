import os
import logging
import boto3
from botocore.exceptions import ClientError

class S3Repository:
    def __init__(self):
        self.s3_client = boto3.client('s3')

    def upload_file(self, file_name, bucket, object_name=None):
        if object_name is None:
            object_name = os.path.basename(file_name)

        try:
            response = self.s3_client.upload_file(file_name, bucket, object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True

    def download_file(self, bucket, object_name, file_name=None):
        if file_name is None:
            file_name = os.path.basename(object_name)

        try:
            self.s3_client.download_file(bucket, object_name, file_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True

    def delete_file(self, bucket, object_name):
        try:
            self.s3_client.delete_object(Bucket=bucket, Key=object_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True
