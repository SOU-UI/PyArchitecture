import unittest
from pyarchitecture.design import Building

class TestDesign(unittest.TestCase):
    def test_calculate_area(self):
        building = Building('TestBuilding', 10, 20, 30)
        self.assertEqual(building.calculate_area(), 200)
    
    def test_calculate_volume(self):
        building = Building('TestBuilding', 10, 20, 30)
        self.assertEqual(building.calculate_volume(), 6000)

if __name__ == '__main__':
    unittest.main()
