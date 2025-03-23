"""
создайте класс `Car`, наследник `Vehicle`
"""
from hw6.base import Vehicle

class Car(Vehicle):
    def __init__(self, weight, fuel, fuel_consuption):
        super().__init__(weight, fuel, fuel_consuption)
        self.engine = None

    def set_engine(self, engine):
        self.engine = engine