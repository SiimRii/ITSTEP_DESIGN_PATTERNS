
# STRUCTURAL

class Legacy:
    def legacy_method(self):
        return "legacy method"



class NewApp:
    def new_method(self):
        pass



class Adapter(NewApp):
    def __init__(self):
        self.legacy = Legacy()

    def new_method(self):
        return self.legacy.legacy_method()



newApp = Adapter()
print(newApp.new_method())