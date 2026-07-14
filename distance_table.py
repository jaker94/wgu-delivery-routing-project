import csv

#create distance table class
class DistanceTable:

    def __init__(self):
        self.addresses = []
        self.addresses_lookup = {}
        self.distances = []

        ##loading the distances and building the lists

    def load_distances(self, filename):
        with open(filename, newline='', encoding='utf-8-sig') as file:
            reader = csv.reader(file)

            #skip the header row
            next(reader)

            for row in reader:

                #splitting addresses from building names to add to address list and removes the leading space // edited to also strip trailing commas
                address = row[0].split("\n")[1].strip().rstrip(",")

                #adding the addresses to the list and the lookup index
                self.addresses.append(address)
                self.addresses_lookup[address] = len(self.addresses) - 1

                #next need to find distances and add them to the distance list
                distance_row = []

                for value in row[2:]:
                    if value == "":
                        distance_row.append(None)
                    else:
                        distance_row.append(float(value))

                self.distances.append(distance_row)

    ## get distance function

    def get_distance(self, address1, address2):
        index1 = self.addresses_lookup[address1]
        index2 = self.addresses_lookup[address2]

        #checks for A -> B distance in the matrix
        distance = self.distances[index1][index2]

        #If A -> B distance is none, checks B -> A
        if distance is None:
            distance = self.distances[index2][index1]

        return distance



