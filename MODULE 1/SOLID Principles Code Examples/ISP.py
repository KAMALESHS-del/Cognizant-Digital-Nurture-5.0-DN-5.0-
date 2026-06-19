from abc import ABC, abstractmethod

class Worker(ABC):

    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

 
class Human(Worker):

    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")


class Robot(Worker):

    def work(self):
        print("Robot working")

    def eat(self):
        print("Robot does not eat")  # Unnecessary
human = Human()
robot = Robot()
human.work()
human.eat()
robot.work()
robot.eat()