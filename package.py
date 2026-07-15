# Creating package class
class Package:
    def __init__(self, id, address, city, state, zip, deadline, kilo, notes):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.kilo = kilo
        self.notes = notes

        self.status = "at the hub"
        self.delivery_time = None
        self.truck_id = None

