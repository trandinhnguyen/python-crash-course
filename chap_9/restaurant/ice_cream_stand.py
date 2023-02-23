from restaurant import Restaurant


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['ngot', 'cay', 'man']

    def get_flavors(self):
        for flavor in self.flavors:
            print(flavor.title())


if __name__ == '__main__':
    my_res = IceCreamStand('nguyen nguyen', 'ice cream stand')
    my_res.get_flavors()
