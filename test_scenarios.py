import unittest
from flask.testing import FlaskClient
from main import app

class FizzBuzzTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_fizzbuzz_endpoint(self):
        # Scenario 1: Basic Fizz-Buzz
        response = self.app.get('/fizzbuzz?int1=3&int2=5&limit=15&str1=fizz&str2=buzz')
        self.assertEqual(response.status_code, 200)
        self.assertListEqual(response.get_json()['result'], [
            '1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz',
            '11', 'fizz', '13', '14', 'fizzbuzz'
        ])

    def test_statistics_endpoint(self):
        # Scenario 2: Check statistics endpoint
        response = self.app.get('/statistics')
        self.assertEqual(response.status_code, 200)
        self.assertIsNone(response.get_json()['most_used_request'])

        # Scenario 3: Update statistics with multiple requests
        self.app.get('/fizzbuzz?int1=3&int2=5&limit=15&str1=fizz&str2=buzz')
        self.app.get('/fizzbuzz?int1=3&int2=5&limit=20&str1=fizz&str2=buzz')
        self.app.get('/fizzbuzz?int1=4&int2=6&limit=10&str1=fizz&str2=buzz')
        self.app.get('/fizzbuzz?int1=3&int2=5&limit=15&str1=fizz&str2=buzz')
        self.app.get('/fizzbuzz?int1=3&int2=5&limit=15&str1=fizz&str2=buzz')
        response = self.app.get('/statistics')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['most_used_request']['parameters'], [3, 5, 15, 'fizz', 'buzz'])
        self.assertEqual(response.get_json()['most_used_request']['hits'], 3)

if __name__ == '__main__':
    unittest.main()
