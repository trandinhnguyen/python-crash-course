food_orders = ['banh mi', 'pho', 'bun', 'banh cuon']
finished_food = []

while food_orders:
    food = food_orders.pop()
    print(f'I made your {food}')
    finished_food.append(food)

print()
for food in finished_food:
    print(food)
