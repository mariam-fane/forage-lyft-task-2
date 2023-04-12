import unittest

from tire.octoprime import Octoprime


class TestDemo(unittest.TestCase):
    def test_needs_service(self):
        tire_data = [0.2, 0.3, 0.1, 0.9]
        tire = Octoprime(tire_data)
        self.assertTrue(tire.needs_service())

    def test_needs_service(self):
        tire_data = [0.1, 0.01, 0.02, 0.2]
        tire = Octoprime(tire_data)
        self.assertFalse(tire.needs_service())