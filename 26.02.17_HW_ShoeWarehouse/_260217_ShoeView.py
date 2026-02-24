


class ShoeView:
    def __init__(self):
        pass


    def added_shoes(self, id):
        print(f"Added shoes - {id}.")


    def didnt_add_shoes(self, id):
        print(f"Couldnt add shoes - {id} because they already exist.")


    def deleted_shoes(self, id):
        print(f"Deleted shoes - {id}.")


    def display_all_shoes(self, all_shoes):
        print(f"Displaying all shoes:")
        i = 1
        for shoes in all_shoes:
            print(f" {i} - shoes with id: {shoes.id}")
            i += 1
        

    def none_shoes_in_specific_size(self, specific_size):
        print(f"No shoes were found in size {specific_size}.")


    def display_shoes_in_specific_size(self, shoes_in_specific_size, specific_size):
        print(f"These are the shoes in size: {specific_size}")
        for shoes in shoes_in_specific_size:
            print(f" - shoes with id: {shoes.id}")


    def none_shoes_in_warehouse(self):
        print("No shoes were found in the warehouse.")


    def display_price_of_all_shoes(self, total_price):
        print(f"Total price of all shoes in the warehouse is: {total_price}.")



