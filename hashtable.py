#Create hashtable class

class Hashtable:
    def __init__(self, capacity=101):
        #number of sorting buckets
        self.capacity = capacity

        #create an empty list for each bucket
        self.table = [[] for _ in range(capacity)]

    #return bucket index for a given key
    def hash_function(self, key):
        return key % self.capacity

    #insert/update a package in the hash table
    def insert(self, package):
        index = self.hash_function(package.id)

        bucket = self.table[index]

        #update package if it already exists
        for i, existing_package in enumerate(bucket):
            if existing_package.id == package.id:
                bucket[i] = package
                return
        #otherwise add the package
        bucket.append(package)

    #find and search by package id
    def search(self, package_id):
        index = self.hash_function(package_id)
        bucket = self.table[index]

        for package in bucket:
            if package.id == package_id:
                return f"Package(\n ID = {package.id},\n Address = {package.address}, \n City = {package.city}, \n State = {package.state}, \n Zip = {package.zip}, \n Deadline = {package.deadline}, \n Weight = {package.kilo}, \n Status = {package.status})"
        return None


    ##allowing the hashtable to look at all packages
    def get_all_packages(self):
        packages = []

        for bucket in self.table:
            for package in bucket:
                packages.append(package)
        return packages
