class Vehicle:
    vehicle_counter = 0

    # pass #use pass to come back to adding in code later
    def __init__(self, body_type, make):
        self.vehicle_body = body_type
        self.make = make
        # below is associated with the class definition
        Vehicle.vehicle_counter += 1

    # note you need to use self arguments to make methods on the class
    def get_vehicle_count(self):
        return Vehicle.vehicle_counter

    def drive(self):
        print('vehicle driving')


# below is how Truck inherits functionality from Vehicle like vehicle_counter
class Truck(Vehicle):
    # notice how we overwrite the method coming from Vehicle parent class
    def drive(self):
        print('truck driving')

class Motorcycle(Vehicle):
    def drive(self):
        print('drive moto fast')
