# Your code below:
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olive","anchovies", "mushrooms"]

prices = [2, 6, 1, 3, 2, 7, 2]

num_two_dollar_slices = prices.count(2)

num_pizzas = len(toppings)

print ( "We sell", num_pizzas, "different kinds of pizza!")

pizza_and_prices = [[2, 'pepperoni'], [6, 'pineapple'], [1, 'cheese'], [3, 'sausage'], [2, 'olives'], [7, 'anchovies'], [2, 'mushrooms']]

print(pizza_and_prices)

pizza_and_prices.sort()

print('\n')
print(pizza_and_prices)

cheapest_pizza = sorted(pizza_and_prices)
print('\n')
print(cheapest_pizza)

priceiest_pizza = pizza_and_prices[-1]
print('\n')
print(priceiest_pizza)
print('\n')
pizza_and_prices.pop()
print(pizza_and_prices)

pizza_and_prices.insert (4,[2.5,'peppers'])
print('\n')
print(pizza_and_prices)

three_cheapest = pizza_and_prices [:3]
print('\n')
print (three_cheapest)



