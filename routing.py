from truck import Truck
from datetime import datetime
from datetime import timedelta

#used in deliver_packages algorithm, declaring all harcoded variables at top of file
TRUCK_SPEED_MPH =18

##creating a load function to handle sorting onto trucks due to constraints, it can't be randomized
def load_trucks(package_table):

    truck1 = Truck(
        truck_id=1,
        start_time=datetime.strptime("08:00", "%H:%M")
    )

    truck2 = Truck(
        truck_id=2,
        start_time=datetime.strptime("08:00", "%H:%M")
    )

    ##2 drivers, 3 loaded trucks. 3rd truck doesn't start at the same time as the others
    truck3 = Truck(
        truck_id=3,
        start_time=None
    )

    truck1_ids = [

    ]

    truck2_ids =[
        3,18,36,38, #truck 2 only
        13,14,15,16,19,20 #must remain together
    ]

    truck3_ids = [
        6,25,28,32, #delayed until 9:05
        9 #address corrected at 10:20
    ]

    add_packages_to_truck(truck1, truck1_ids, package_table)
    add_packages_to_truck(truck2, truck2_ids, package_table)
    add_packages_to_truck(truck3, truck3_ids, package_table)

    return truck1, truck2, truck3

def add_packages_to_truck(truck, package_ids, package_table):
    for package_id in package_ids:
        package = package_table.search(package_id)

        if package is None:
            raise ValueError(f"Package {packpage_id} was not found.")

        truck.add_package(package)

def deliver_packages(truck, distance_table):
    while truck.packages:
        nearest_package = None
        nearest_distance = float("inf")

        #find the closest remaining package
        for package in truck.packages:
            #passing starting and ending locations to get distance
            distance = distance_table.get_distance(
            truck.current_address,
            package.address
            )
            #checking if it's the closest distance
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_package = package

        #travel to the selected package
        truck.mileage += nearest_distance

        #taking distance / speed and updating current time
        travel_hours = nearest_distance / TRUCK_SPEED_MPH
        truck.current_time += timedelta(hours = travel_hours)

        #move the truck to the delivery address
        truck.current_address = nearest_package.address

        #recording the delivery
        nearest_package.status = "Delivered"
        nearest_package.delivery_time = truck.current_time
        nearest_package.truck_id = truck.truck_id

        #moving the package to the delivered status to remove it from the delivery queue
        truck.packages.remove(nearest_package)
        truck.delivered_packages.append(nearest_package)




