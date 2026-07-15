#  Name: Jacob Register Student ID: 012661699
from hashtable import Hashtable
from package import Package
from csv_loader import load_packages
from truck import Truck
from routing import load_trucks, deliver_packages
from datetime import datetime
from distance_table import DistanceTable

def main():

    # Create hash table
    package_table = Hashtable()

    #load the packages into the hash table
    load_packages(
        "WGUPS Package File - Sheet1.csv",
        package_table
    )

    #testing it worked
    package = package_table.search(15)

    #create the distance table
    distance_table = DistanceTable()
    distance_table.load_distances("WGUPS Distance Table (1) - Sheet1.csv")

    #create truck objects and load them
    truck1, truck2, truck3 = load_trucks(package_table)

    #start delivery
    deliver_packages(truck1, distance_table)
    deliver_packages(truck2, distance_table)

    #figured out when truck 3 can leave
    delayed_ready_time = datetime.strptime("9:05", "%H:%M")

    #set truck3 time to driver availability time

    truck3.start_time = max(
        min(truck1.current_time, truck2.current_time),
        delayed_ready_time
    )

    #update current time to truck 3 start time
    truck3.current_time = truck3.start_time

    deliver_packages(truck3, distance_table)

    #temp tracking currently assigned packages
    assigned = {
        3, 6, 9, 13, 14, 15, 16, 18, 19, 20,
        25, 28, 32, 36, 38
    }


if __name__ == "__main__":
    main()