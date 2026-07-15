from truck import Truck
from datetime import datetime
from datetime import timedelta

#used in deliver_packages algorithm, declaring all harcoded variables at top of file
TRUCK_SPEED_MPH =18

##creating a load function to handle sorting onto trucks due to constraints, it can't be randomized
def load_trucks(package_table, distance_table):

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

    #manually setting the IDs with constraints
    truck1_ids =[
        29, 7, #same address, 1 with deadline
        30, 31, 34 #packages with deadlines
    ]



    #manually setting the IDs with constraints
    truck2_ids =[
        3,18,36,38, #truck 2 only
        13,14,15,16,19,20 #must remain together
    ]
    #manually settings the IDs with constraints
    truck3_ids = [
        6,25,28,32, #delayed until 9:05
        9 #address corrected at 10:20
    ]

    #prepping to assign ids using nearest neighbor loading algorithm
    assigned_ids = set()

    #add packages to truck, taking into account manually placed packages, and the remaining unassigned packages
    add_packages_to_truck(
        truck1,
        truck1_ids,
        package_table
    )

    #update the assigned IDs so the algorithm knows which ones are remaining
    assigned_ids.update(truck1_ids)

    add_packages_to_truck(
        truck2,
        truck2_ids,
        package_table
    )

    assigned_ids.update(truck2_ids)

    add_packages_to_truck(
        truck3,
        truck3_ids,
        package_table
    )

    assigned_ids.update(truck3_ids)

    assign_remaining_packages(
        package_table,
        distance_table,
        truck1,
        truck2,
        truck3,
        assigned_ids
    )

    return truck1, truck2, truck3

#adding packages from the id lists to the trucks
def add_packages_to_truck(truck, package_ids, package_table):
    for package_id in package_ids:
        package = package_table.search(package_id)

        if package is None:
            raise ValueError(f"Package {packpage_id} was not found.")

        truck.add_package(package)

#building an algorithm to assign the remaining packages based on distance

def assign_remaining_packages(
        package_table,
        distance_table,
        truck1,
        truck2,
        truck3,
        assigned_ids
):
    remaining_packages = [
        package
        for package in package_table.get_all_packages()
            if package.id not in assigned_ids
    ]

    for package in remaining_packages:
        eligible_trucks = [
            truck
            for truck in (truck1, truck2, truck3)
            if len(truck.packages) < 16
        ]

        best_truck = None
        best_distance = float("inf")

        for truck in eligible_trucks:
            #if the truck is empty, compare the package to the hub
            if not truck.packages:
                distance = distance_table.get_distance(
                    truck.current_address,
                    package.address
                )
            else:
                #find the closest address already assigned to the truck
                distance = min(
                    distance_table.get_distance(
                        existing_package.address,
                        package.address
                    )
                    for existing_package in truck.packages
                )

            if distance < best_distance:
                best_distance = distance
                best_truck = truck

        if best_truck is None:
            raise ValueError(
                f"No truck as capacity for package {package.id}"
            )

        best_truck.add_package(package)
        assigned_ids.add(package.id)

#nearest neighbor algorithm for delivering packages
def deliver_packages(truck, distance_table):
    address_correction_time = datetime.strptime("10:20", "%H:%M")
    while truck.packages:
        nearest_package = None
        nearest_distance = float("inf")

        #find the closest remaining package
        for package in truck.packages:
            if package.id == 9:
                if truck.current_time < address_correction_time:
                    continue

                package.address = "410 S State St"
                package.zip = "84111"

            #passing starting and ending locations to get distance
            distance = distance_table.get_distance(
                truck.current_address,
                package.address
            )
            #checking if it's the closest distance
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_package = package

        if nearest_package is None:
            truck.current_time = address_correction_time
            continue

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

    #the truck 3 start time was logged as the same time as the last delivery even though the driver wasn't back to hub, this function is to calculate that. Also flagged an issue where total mileage didn't account for trucks returning to hub
def return_to_hub(truck, distance_table):
    hub_address = "4001 South 700 East"

    #trucks current location -> back to hub
    distance = distance_table.get_distance(
        truck.current_address,
        hub_address
    )

    #increment truck mileage
    truck.mileage += distance

    #increment travel distance
    travel_hours = distance / TRUCK_SPEED_MPH
    truck.current_time += timedelta(hours = travel_hours)

    #update truck location
    truck.current_address = hub_address




