class Car:

    def drive(self):
        print("Driving Car")


class Bike:

    def drive(self):
        print("Riding Bike")


class VehicleFactory:

    def create_vehicle(self, vehicle_type):

        if vehicle_type == "car":
            return Car()

        elif vehicle_type == "bike":
            return Bike()


factory = VehicleFactory()

vehicle1 = factory.create_vehicle("car")
vehicle1.drive()

vehicle2 = factory.create_vehicle("bike")
vehicle2.drive()