from trebuchet import calibrationData
import unittest


class TestData(unittest.TestCase):

    def test_calibrationData(self):
        self.assertEqual(calibrationData(), 54573, "Should be 54573")

if __name__ == '__main__':
    unittest.main()