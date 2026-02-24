


class ShoeModel:
    def __init__(self):
        self.shoes = []


    # working with data:
    def adding_shoes(self, shoes):
        if shoes.id not in [shoe.id for shoe in self.shoes]:
            self.shoes.append(shoes)
            return True
        return False


    def is_deleted_shoes(self, id):
        shoe_to_be_deleted = self.get_shoes(id)
        if shoe_to_be_deleted is not None:
            self.shoes.remove(shoe_to_be_deleted)
            return True
        else:
            return False
        

    def get_shoes(self, id):
        for shoe in self.shoes:
            if shoe.id == id:
                return shoe


    def get_all_shoes(self):
        return self.shoes


    # displaying information:
    def displaying_shoes_in_specific_size(self, specific_size):
        shoes_in_specific_size = []
        for shoes in self.shoes:
            if shoes.size == specific_size:
                shoes_in_specific_size.append(shoes)
        return shoes_in_specific_size if shoes_in_specific_size else None


    # getting information:
    def getting_price_of_all_shoes(self):
        total_price = 0
        for shoes in self.shoes:
            total_price += shoes.price
        return total_price

