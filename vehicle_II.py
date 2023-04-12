from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Truck(Vehicle):
    def start(self):
        print("Truck started")


my_truck = Truck()
my_truck.start()
