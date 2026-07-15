# Creating truck class
from datetime import datetime

class Truck:
    def __init__(self, truck_id, start_time):
        self.truck_id = truck_id
        self.location = "4001 South 700 East" # hub
        self.mileage = 0.0
        self.current_time = start_time

    ##added a failsafe to ensure one truck doesn't get more than 16 packages
    def add_package(self, package):
        if len(self.packages) >= 16:
            raise ValueError("Truck is full")

        self.packages.append(package)
