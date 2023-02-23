from car import Car
from battery import Battery


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


if __name__ == '__main__':
    my_car = ElectricCar('idk', 'honda', 2023)
    my_car.battery.get_range()
    my_car.battery.upgrade_battery()
    my_car.battery.get_range()
