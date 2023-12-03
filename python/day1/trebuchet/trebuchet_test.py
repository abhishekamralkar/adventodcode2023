from trebuchet import calibrationDataTotal
import unittest


class TestData(unittest.TestCase):

    def test_calibrationDataTotal(self):
        self.assertEqual(calibrationDataTotal(), 54573, "Should be 54573")

if __name__ == '__main__':
    unittest.main()