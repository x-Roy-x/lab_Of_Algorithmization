from insurances.Life import *
from insurances.Car import *
from Broker import *
from insurances.Health import *
from insurances.House import *


if __name__ == '__main__':
    broker = Broker()

    life = Life("Name", 18, 60, 14000, 5, "personal")
    health = Health("Name", "healthy", 50, 10000, 3, "personal")
    car = Car("Name", 5, 35, 8000, 3, "personal")
    house = House("Name", "private", 40, 9000, 4, "personal")

    broker.insurances = [life, health, car, house]
    print("Previous list:")
    broker.print_list()

    broker.sort_by_risk()
    print("Sorted list")
    broker.print_list()
