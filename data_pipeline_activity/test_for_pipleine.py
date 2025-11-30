import unittest
import numpy as np
from unit_test.line_fitting_pipeline import generated_data, line_of_fit, predicted_values


class my_unit_tests(unittest.TestCase):

    # Test line_of_fit function for accuracy
    def test_line_of_fit_accuracy(self):
        x = np.arange(1, 11)
        y = 3 * x + 10   # true slope=3, intercept=10

        slope, intercept = line_of_fit(x, y)

        # Check slope and intercept match expected values
        self.assertAlmostEqual(slope, 3.0, places=6)
        self.assertAlmostEqual(intercept, 10.0, places=6)

    # Test predicted_values function for correctness
    def test_predict_function(self):
        slope, intercept = 3, 10
        x = np.array([1, 2, 3])

        expected = np.array([13, 16, 19])
        actual = predicted_values(x, slope, intercept)

        # Compare element-wise
        self.assertTrue(np.allclose(actual, expected))

    # Test generated_data function for correct output shape
    def test_generated_data_shape(self):
        x, y = generated_data(n=12)

        self.assertEqual(len(x), 12)
        self.assertEqual(len(y), 12)


if __name__ == "__main__":
    unittest.main()

