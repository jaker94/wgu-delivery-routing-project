# Creating truck class
from datetime import datetime

class Truck:
    def __init__(self, truck_id, start_time):
        self.truck_id = truck_id
        self.packages = []
        self.delivered_packages = []
        self.current_address = "4001 South 700 East" # hub
        self.mileage = 0.0
        self.start_time = start_time
        self.current_time = start_time

    #split this into it's own function so i can add the 16 package limit constraint to the trucks
    def add_package(self, package):
        if len(self.packages) >= 16:
            raise ValueError("Truck is full")

        self.packages.append(package)