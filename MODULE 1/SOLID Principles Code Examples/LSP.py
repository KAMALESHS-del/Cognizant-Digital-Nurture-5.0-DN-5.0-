class Bird:

    def fly(self):
        print("Bird is flying")


class Penguin(Bird):

    def fly(self):
        raise Exception("Penguins cannot fly")


bird = Penguin()
bird.fly()

