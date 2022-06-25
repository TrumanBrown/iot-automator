import unittest.mock
import unittest
import sys
sys.path.append('/mnt/c/Users/linct/Desktop/Code/TrumanBrown/iot-automator/truman')
print(sys.path)
from truman import checkName


class Test_Main(unittest.TestCase):
    print(sys.path)
    def test_checkName(self):
        response=checkName("Truman")
        self.assertEqual(response, "Awesome! :)")

if __name__ == '__main__':
    unittest.main()