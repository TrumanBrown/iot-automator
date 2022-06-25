import unittest.mock
import unittest
import sys
sys.path.append('../truman')
from truman import checkName


class Test_Main(unittest.TestCase):
    print(sys.path)
    def test_checkName(self):
        response=checkName("Truman")
        self.assertEqual(response, "Awesome! :)")

if __name__ == '__main__':
    unittest.main()