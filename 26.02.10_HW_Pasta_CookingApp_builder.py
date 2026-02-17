

class Pasta:
    def __init__(self, pasta_type, sauce, topping, dressing):
        self.pasta_type = pasta_type
        self.sauce = sauce
        self.topping = topping
        self.dressing = dressing

    def __str__(self):
        return (
            f"Type: {self.pasta_type}\n"
            f"Sauce: {self.sauce}\n"
            f"Topping: {self.topping}\n"
            f"Dressing: {self.dressing}\n"
        )


##############################

class PastaBuilder:
    def __init__(self):
        self.pasta_type = None
        self.sauce = None
        self.topping = None
        self.dressing = None

    def set_pasta_type(self, pasta_type):
        self.pasta_type = pasta_type
        return self

    def set_sauce(self, sauce):
        self.sauce = sauce
        return self

    def set_topping(self, topping):
        self.topping = topping
        return self

    def set_dressing(self, dressing):
        self.dressing = dressing
        return self

    def build(self):
        return Pasta(
            self.pasta_type,
            self.sauce,
            self.topping,
            self.dressing
        )


class PastaDirector:
    def __init__(self, builder):
        self.builder = builder

    def cook_carbonara(self):
        return (
            self.builder
            .set_pasta_type("Spaghetti")
            .set_sauce("Carbonara")
            .set_dressing("Olive oil")
            .set_topping("Bacon and Parmesan")
            .build())

    def cook_bolognese(self):
        return (
            self.builder
            .set_pasta_type("Penne")
            .set_sauce("Bolognese")
            .set_dressing("Basil")
            .set_topping("Beef and Cheese")
            .build())


##############################

cooking_director = PastaDirector(PastaBuilder())

carbonara = cooking_director.cook_carbonara()
bolognese = cooking_director.cook_bolognese()

print("\nDisplaying what pastas available:\n")
print(carbonara)
print(bolognese)
    

