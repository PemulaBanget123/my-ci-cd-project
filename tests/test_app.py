import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app import app  # Now app.py can be imported correctly

class TestApp(unittest.TestCase):
    def test_home(self):
        response = app.test_client().get('/')
        self.assertEqual(response.data, b'Hello, World!')

if __name__ == "__main__":
    unittest.main()
