import math
import unittest
from datetime import date, datetime

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from car_factory import CarFactory
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine



        
class TestDemo(unittest.TestCase):



    def test_battery_should_be_serviced(self):
        current_date = date.fromisoformat("2023-01-01")
        last_service_date =  date.fromisoformat("2020-01-01")
        battery = SpindlerBattery(current_date, last_service_date)

        self.assertTrue(battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        current_date = date.fromisoformat("2023-01-01")
        last_service_date =  date.fromisoformat("2022-01-01")
        battery = SpindlerBattery(current_date, last_service_date)

        self.assertFalse(battery.needs_service())

    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())


    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())
    

if __name__ == "__main__":
    unittest.main()