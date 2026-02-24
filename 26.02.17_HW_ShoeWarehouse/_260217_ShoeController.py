
from _260217_Shoe import Shoe


class ShoeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view


    # working with data:
    def add_shoes(self, id, gender_type, type, color, price, brand, size):
        shoes = Shoe(id, gender_type, type, color, price, brand, size)
        if self.model.adding_shoes(shoes):
            self.view.added_shoes(shoes.id)
        else:
            self.view.didnt_add_shoes(shoes.id)


    def delete_shoes(self, id):
        if self.model.is_deleted_shoes(id):
            self.view.deleted_shoes(id)


    # displaying information:
    def display_all_shoes(self):
        all_shoes = self.model.get_all_shoes() 
        self.view.display_all_shoes(all_shoes)


    def display_shoes_in_specific_size(self, specific_size):
        shoes_in_specific_size = self.model.displaying_shoes_in_specific_size(specific_size)

        if shoes_in_specific_size is None:
            self.view.none_shoes_in_specific_size(specific_size)
        else:
            self.view.display_shoes_in_specific_size(shoes_in_specific_size, specific_size)


    # getting information:
    def get_price_of_all_shoes(self):
        total_price = self.model.getting_price_of_all_shoes()
        if total_price == 0:
            self.view.none_shoes_in_warehouse()
        elif total_price > 0:
            self.view.display_price_of_all_shoes(total_price)



