
# STRUCTURAL

class Drink:
    def price(self):
        raise NotImplementedError


class Coffee(Drink):
    def price(self):
        return 4


class Tea(Drink):
    def price(self):
        return 3



class AddingDecorator(Drink):
    def __init__(self, drink):
        self._drink = drink     #set as 'protected', only convention tho

    def price(self):                   
        return self._drink.price()


class Milk(AddingDecorator):
    def price(self):
        return super().price() + 1


class Sugar(AddingDecorator):
    def price(self):
        return super().price() + 0.50




my_coffee1 = Coffee()
my_coffee2 = Coffee()
my_coffee3 = Coffee()
my_tea = Tea()

print(f"basic coffee: {my_coffee1.price()} €")
print(f"basic tea: {my_tea.price()} €\n")

my_coffee1 = Milk(my_coffee1)
my_coffee2 = Sugar(my_coffee2)
my_coffee3 = Milk(Sugar(my_coffee3))
my_tea = Sugar(my_tea)

print(f"coffe with milk: {my_coffee1.price()} €")
print(f"coffee with sugar: {my_coffee2.price()} €")
print(f"coffee with milk + sugar: {my_coffee3.price()} €\n")
print(f"tea with sugar: {my_tea.price()} €")
