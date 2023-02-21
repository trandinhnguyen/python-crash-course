food_orders = ['banh mi', 'pho', 'bun',
               'banh cuon', 'com rang', 'com rang', 'com rang']
finished_food = []
run_out_of_food = 'com rang'

print(f'Run out of {run_out_of_food}')
while run_out_of_food in food_orders:
    food_orders.remove(run_out_of_food)

print()
while food_orders:
    food = food_orders.pop()
    print(f'I made your {food}')
    finished_food.append(food)

print()
for food in finished_food:
    print(food)
