import boto3
from moto import mock_aws
import unittest

# client = boto3.client('ec2')

# response = client.describe_snapshots(OwnerIds=['self'])

# print(response)

def create_bucket(bucket_name):
    s3 = boto3.client('s3')
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'eu-west-1',
        },
    )

    response3 = s3.list_buckets()
    return response3['Buckets'][0]['Name']

class TestCases(unittest.TestCase):

    @mock_aws
    def test_s3_bucket(self):
        bucket_name = 'example'
        response = create_bucket(bucket_name)
        print("Completed")
        assert response == bucket_name
    
if __name__ == '__main__':
    unittest.main()
