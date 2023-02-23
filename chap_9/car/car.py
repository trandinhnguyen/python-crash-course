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
