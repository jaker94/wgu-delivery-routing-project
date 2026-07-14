# Creating truck class
from datetime import datetime

class Truck:
    def __init__(self, truck_id, start_time):
        self.truck_id = truck_id
        self.packages = []
        self.location = "4001 South 700 East" # hub
        self.mileage = 0.0
        self.current_time = start_time

