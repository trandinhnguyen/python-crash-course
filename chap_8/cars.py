def make_car(manufacturer, model, **kwagrs):
    kwagrs['manufacturer'] = manufacturer
    kwagrs['model'] = model
    return kwagrs


car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)

my_car = make_car('lamborghini', 'aventador', color='green', year=2023)
print(my_car)
