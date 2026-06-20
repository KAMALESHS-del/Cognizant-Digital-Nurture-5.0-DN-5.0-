class Computer:

    def __init__(self):
        self.cpu = None
        self.ram = None
        self.ssd = None
        self.keyboard = None
        self.mouse = None

    def show(self):
        print("CPU:", self.cpu)
        print("RAM:", self.ram)
        print("SSD:", self.ssd)
        print("Keyboard:", self.keyboard)
        print("Mouse:", self.mouse)
class ComputerBuilder:

    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_ssd(self, ssd):
        self.computer.ssd = ssd
        return self

    def set_keyboard(self, keyboard):
        self.computer.keyboard = keyboard
        return self

    def set_mouse(self, mouse):
        self.computer.mouse = mouse
        return self

    def build(self):
        return self.computer


computer = (ComputerBuilder()
            .set_cpu("Intel i7")
            .set_ram("16GB")
            .set_ssd("512GB SSD")
            .set_keyboard("Mechanical Keyboard")
            .set_mouse("Wireless Mouse")
            .build())
computer.show()