

class Singleton:
    #atribute of singleton, exists only one such object
    object = None

    @staticmethod
    def getInstance():
        if Singleton.object is None:
            Singleton.object = Singleton()
        return Singleton.object




object1 = Singleton().getInstance()
print(object1)

object2 = Singleton().getInstance()
print(object2)

