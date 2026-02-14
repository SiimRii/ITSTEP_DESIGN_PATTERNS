
# BEHAVIORAL

def no_discount(price):
    return price


def percentual_discount(price):
    return price * 0.9


def fixed_discount(price):
    return price - 100 if price > 100 else price



class ShoppingCart:
    def __init__(self, price, discount_strategy = no_discount):
        self.price = price
        self.discount_strategy = discount_strategy

    def set_strategy(self, new_strategy):
        self.discount_strategy = new_strategy

    def calculate_price(self):
        return self.discount_strategy(self.price)



cart = ShoppingCart(500)
print(f"Primal price: {cart.price}")
print(f"Price after discount: {cart.calculate_price()}")

cart.set_strategy(percentual_discount)
print(f"Price after percentual discount: {cart.calculate_price()}")

cart.set_strategy(fixed_discount)
print(f"Price after fixed discount: {cart.calculate_price()}")


