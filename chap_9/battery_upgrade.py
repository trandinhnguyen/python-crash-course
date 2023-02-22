class Car:
    """ A simple attempt to represent a Car """

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name

    def read_odometer(self):
        """Print mileage"""
        print(f'This car has {self.odometer_reading} miles on it')

    def update_odometer(self, mileage):
        """Set the odometer"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Can't roll back an odometer")

    def increment_odometer(self, miles):
        """Add to the odometer reading"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("Can't roll back an odometer")


class Battery:
    def __init__(self, battery_size=40) -> None:
        self.battery_size = battery_size

    def describe_battery(self):
        print(f'This car has a {self.battery_size}-kWh battery')

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f'This car can go about {range} miles on a full charge')

    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


if __name__ == '__main__':
    my_car = ElectricCar('idk', 'honda', 2023)
    my_car.battery.get_range()
    my_car.battery.upgrade_battery()
    my_car.battery.get_range()
