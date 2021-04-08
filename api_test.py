import unittest, requests
from app import app

class FlaskTest(unittest.TestCase):
    API_URL_TEST = "http://localhost:5000/get?word=foobar"
    API_URL = "http://localhost:5000/load"
    ANAGRAM_LIST = {
        "load": ["foobar", "test", "aabb", "abab"]
    }
    def test_post_anagram(self):
        r = requests.put(FlaskTest.API_URL, json=FlaskTest.ANAGRAM_LIST)
        self.assertEqual(r.status_code, 200)

    def test_get_anagram(self):
        r = requests.get(FlaskTest.API_URL_TEST)
        self.assertEqual(r.status_code, 200)

if __name__ == "__main__":
    unittest.main() 




        