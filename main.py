#  Name: Jacob Register Student ID: 012661699
from hashtable import Hashtable
from package import Package
from csv_loader import load_packages
from truck import Truck
from datetime import datetime

def main():

    # Create hash table
    package_table = Hashtable()

    load_packages(
        "WGUPS Package File - Sheet1.csv",
        package_table
    )

    package = package_table.search(15)

    print(package)


if __name__ == "__main__":
    main()