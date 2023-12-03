from trebuchet import calibrationDataTotal
import unittest

# def test_calibrationDataTotal():
#     assert calibrationDataTotal() == 54573, "Should be 54473"

# if __name__ == "__main__":
#     test_calibrationDataTotal()
#     print("Calibration Data Looks Good Now!")


# import unittest


class TestData(unittest.TestCase):

    def test_calibrationDataTotal(self):
        self.assertEqual(calibrationDataTotal(), 54573, "Should be 54473")

if __name__ == '__main__':
    unittest.main()