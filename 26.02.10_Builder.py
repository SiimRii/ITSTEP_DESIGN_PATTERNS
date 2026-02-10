
# CREATIONAL

class Computer:
    def __init__(self, cpu, gpu, ram, storage, power, color, case_brand):
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram
        self.storage = storage
        self.power = power
        self.color = color
        self.case_brand = case_brand

    def __str__(self):
        return f"CPU: {self.cpu}\nGPU: {self.gpu}\nRAM: {self.ram}\nStorage: {self.storage}\nPower: {self.power}\nColor: {self.color}\nCase brand: {self.case_brand}\n"



class ComputerBuilder:
    def __init__(self):
        self.cpu = None
        self.gpu = None
        self.ram = None
        self.storage = None
        self.power = None
        self.color = None
        self.case_brand = None

    
    def add_cpu(self, cpu):
        self.cpu = cpu

    def add_gpu(self, gpu):
        self.gpu = gpu

    def add_ram(self, ram):
        self.ram = ram

    def add_storage(self, storage):
        self.storage = storage

    def add_power(self, power):
        self.power = power

    def add_color(self, color):
        self.color = color

    def add_case_brand(self, case_brand):
        self.case_brand = case_brand


    def build(self):
        return Computer(self.cpu, self.gpu, self.ram, self.storage, self.power, self.color, self.case_brand)



##########

computer1 = Computer("Intel", "Nvidia", "16GB", "1TB", "Black", "15W", "Asus")

computerBuilder = ComputerBuilder()
computerBuilder.add_storage("2TB")
computerBuilder.add_ram("32GB")
computerBuilder.add_power("20W")

computer2 = computerBuilder.build()

print(computer1)
print(computer2)

