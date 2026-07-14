#  Student ID: 012661699

from hashtable import Hashtable
from package import Package
from truck import Truck
from datetime import datetime

def main():

    # Create hash table
    package_table = Hashtable()

    # Create a test package
    package = Package(
        1,
        "195 W Oakland Ave",
        "Salt Lake City",
        "UT",
        "84115",
        "10:30 AM",
        21,
        ""
    )

    # Insert package into hash table
    package_table.insert(package)

    # Search for package
    result = package_table.search(1)

    print(result.address)


if __name__ == "__main__":
    main()