import csv
from package import Package

#creating the load CSV as a function
def load_packages(filename, hash_table):
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)

        next(reader)

        for row in reader:
            package = Package(
                int(row[0]),
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                int(row[6]),
                row[7]
            )

            hash_table.insert(package)
