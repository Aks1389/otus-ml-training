from abc import ABC
from hw6.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight, fuel, fuel_consuption):
        super().__init__()
        self.weight = weight
        self.fuel = fuel # L
        self.fuel_consuption = fuel_consuption #  L/100
        self.started = False

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError()
    
    def move(self, distance):
        travel_consumption = distance * self.fuel_consuption
        fuel_left = self.fuel - travel_consumption
        if fuel_left < 0:
            raise NotEnoughFuel()