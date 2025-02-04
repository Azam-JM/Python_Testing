class Car:
    def drive(self):
        return "Engine started"

def function_to_test():
    car = Car()
    return car.drive()


# Unittest
import unittest
from unittest.mock import patch
class TestCases(unittest.TestCase):
    def test_validation(self):
        with patch.object(Car, 'drive', return_value="Car Stopped") as carObject:
            # carObject.return_value = "Car Started"
            response = function_to_test()
            assert response == "Car Stopped"
            carObject.assert_called_once()

if __name__ == '__main__':
    unittest.main()
