import unittest.mock
import unittest
import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'truman'))
print(sys.path)
from truman import checkName


class Test_Main(unittest.TestCase):
    print(sys.path)
    def test_checkName(self):
        response=checkName("Truman")
        self.assertEqual(response, "Awesome! :(")

if __name__ == '__main__':
    unittest.main()