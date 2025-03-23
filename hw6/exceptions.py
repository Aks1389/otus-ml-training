"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class LowFuelError(Exception):
    def __init__(self, message="Недостаточно топлива для старта двигателя!"):
        self.message = message
        super().__init__(self.message)

class NotEnoughFuel(Exception):
    def __init__(self, message="Недостаточно топлива для преодоления дистанции!"):
        self.message = message
        super().__init__(self.message)

class VehicleOverload(Exception):
    def __init__(self, message="Транспорт перегружен!"):
        self.message = message
        super().__init__(self.message)