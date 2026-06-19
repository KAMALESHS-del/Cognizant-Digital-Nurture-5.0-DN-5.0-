class Bird:
    pass


class FlyingBird(Bird):

    def fly(self):
        print("Bird is flying")


class Sparrow(FlyingBird):
    pass


class Eagle(FlyingBird):
    pass


class Penguin(Bird):

    def swim(self):
        print("Penguin is swimming")
sparrow = Sparrow()
sparrow.fly()

penguin = Penguin()
penguin.swim()        