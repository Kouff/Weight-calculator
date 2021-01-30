import unittest
from weight_calculator import calculate_weight


class TestCalculator(unittest.TestCase):
    def test_calculate_weight(self):
        data = [
            {'id': 1, 'weight': 1, 'elems': [2, 3]},
            {'id': 2, 'weight': 2, 'elems': []},
            {'id': 3, 'weight': 3, 'elems': [4]},
            {'id': 4, 'weight': 4, 'elems': []},
            {'id': 5, 'weight': 5, 'elems': [1]}
        ]
        self.assertEqual(
            calculate_weight(data),
            {1: 10, 2: 2, 3: 7, 4: 4, 5: 15}
        )


if __name__ == "__main__":
    unittest.main()
