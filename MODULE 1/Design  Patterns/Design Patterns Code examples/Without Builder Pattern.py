class Computer:

    def __init__(self, cpu, ram, ssd, keyboard, mouse):
        self.cpu = cpu
        self.ram = ram
        self.ssd = ssd
        self.keyboard = keyboard
        self.mouse = mouse

    def show(self):
        print("CPU:", self.cpu)
        print("RAM:", self.ram)
        print("SSD:", self.ssd)
        print("Keyboard:", self.keyboard)
        print("Mouse:", self.mouse)


computer = Computer(
    "Intel i7",
    "16GB",
    "512GB SSD",
    "Mechanical Keyboard",
    "Wireless Mouse"
)

computer.show()