import unittest
from main import Rectangulo, Circulo

class TestRectangulo(unittest.TestCase):
    def test_area(self):
        rectangulo = Rectangulo(4, 5)
        self.assertEqual(rectangulo.area(), 20)

class TestCirculo(unittest.TestCase):
    def test_area(self):
        circulo = Circulo(3)
        self.assertAlmostEqual(circulo.area(), 28.274333882308138, places=6)

if __name__ == '__main__':
    unittest.main()
