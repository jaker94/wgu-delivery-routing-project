#  Name: Jacob Register Student ID: 012661699
from hashtable import Hashtable
from package import Package
from csv_loader import load_packages
from truck import Truck
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

    print(package)

    distance_table = DistanceTable()
    distance_table.load_distances("WGUPS Distance Table (1) - Sheet1.csv")

    distance = distance_table.get_distance(
        "4001 South 700 East",
        "195 W Oakland Ave"
    )

    print(distance)
if __name__ == "__main__":
    main()