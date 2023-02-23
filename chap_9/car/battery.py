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
