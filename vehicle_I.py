from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    def beep(self):
        print("Beep beep!")


class Car(Vehicle):
    def start(self):
        print("Starting the car.")

    def stop(self):
        print("Stopping the car.")

my_car = Car()

my_car.start()
my_car.stop()
my_car.beep()