"""
создайте класс `Plane`, наследник `Vehicle`
"""

from hw6.base import Vehicle
from hw6.exceptions import VehicleOverload

class Plane(Vehicle):
    def __init__(self, weight, fuel, fuel_consuption, max_cargo):
        super().__init__(weight, fuel, fuel_consuption)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, cargo_amount):
        if self.cargo + cargo_amount >= self.max_cargo:
            overload = self.max_cargo - (self.cargo + cargo_amount)
            raise VehicleOverload(f"Самолет перегружен на {overload}")
        else:
            self.cargo += cargo_amount

    def remove_all_cargo(self):
        cargo_before_purge = self.cargo
        self.cargo = 0
        return cargo_before_purge