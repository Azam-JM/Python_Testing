import boto3.session

def do_stuff():
    session = boto3.session.Session()
    client = session.client(service_name="secretsmanager", region_name='myregion')
    return client.get_secret_value(SecretId='some-secret-id')

from unittest.mock import patch, MagicMock
import unittest
from session import do_stuff

class TestCase(unittest.TestCase):
    @patch('boto3.session.Session')
    def test_session(self, mock_session):
        mock_client = MagicMock()
        mock_client.get_secret_value.return_value = {
            'SecretString': 'my-secret'
        }
        mock_session.return_value.client.return_value = mock_client


        result = do_stuff()
        assert 'my-secret'== result['SecretString']

if __name__ == '__main__':
    unittest.main()
