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


if __name__ == '__main__':
    my_res = Restaurant('nguyen', 'hot pot')
    my_res.increase_number_served(100)
    print(my_res.number_served)
