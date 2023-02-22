class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 10

    def describe_restaurant(self):
        print(f'{self.restaurant_name} {self.cuisine_type}')

    def open_restaurant():
        print('The restaurant is open')

    def set_number_served(self, n):
        if n >= self.number_served:
            self.number_served = n
        else:
            print("Can't roll back")

    def increase_number_served(self, n):
        if n >= 0:
            self.number_served += n
            print('A day of business')
        else:
            print("Can't roll back")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['ngot', 'cay', 'man']

    def get_flavors(self):
        for flavor in self.flavors:
            print(flavor.title())


my_res = IceCreamStand('nguyen nguyen', 'ice cream stand')
my_res.get_flavors()
