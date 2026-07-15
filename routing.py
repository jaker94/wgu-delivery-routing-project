from truck import Truck
from datetime import datetime

##creating a load function to handle sorting onto trucks due to constraints, it can't be randomized
def load_trucks(package_table)

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

    return truck1, truck2, truck3