import csv
from package import Package

#fixing an address that was getting abbreviated
ADDRESS_CORRECTIONS = {
    "3575 W Valley Central Station bus Loop":
        "3575 W Valley Central Sta bus Loop"
}

#creating the load CSV as a function
def load_packages(filename, hash_table):

    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        #skip the header row
        next(reader)

        #grabs the data and assigns them row values in the table
        for row in reader:
            address = row[1].strip()
            address = ADDRESS_CORRECTIONS.get(address, address)

            package = Package(
                int(row[0]),
                address,
                row[2].strip(),
                row[3].strip(),
                row[4].strip(),
                row[5].strip(),
                int(row[6]),
                row[7].strip()
            )
            #inserts them into the table
            hash_table.insert(package)
